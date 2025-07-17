
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from app.api.v1.schemas.auth import SendOtpRequest
from app.db.session import get_db
from app.services.send_message_serice import send_otp_sms
from utils.generate_otp import generate_otp
from utils.store_otp import store_otp



router = APIRouter()

@router.post("/send-otp")
async def send_otp(payload: SendOtpRequest, db: Session = Depends(get_db)):
    phone_number = payload.phone_number

    otp = generate_otp()

    store_otp['phone_number'] = phone_number
    store_otp['otp'] = otp
    store_otp['create_at'] = datetime.now().isoformat()

    query = text("SELECT * FROM auth_identifier WHERE identifier = :identifier")
    try:
        auth_identifier = db.execute(query,{"identifier": phone_number}).fetchone()

        if not auth_identifier:
            db.execute(text("INSERT INTO auth_identifier (identifier,is_verified, is_registered,is_active) VALUES (:identifier, :is_verified, :is_registered, :is_active)"),{"identifier": phone_number,"is_verified": False,"is_registered": False, "is_active": False})
            db.commit()
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=500,detail="Database error")

    is_success = send_otp_sms(phone_number=phone_number,otp=otp)
    if is_success:
        return {"message": "OTP sent successfully"}
    
    raise HTTPException(status_code=500,detail="Failed to send OTP")