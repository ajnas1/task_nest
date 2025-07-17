
from datetime import datetime
from fastapi import APIRouter

from app.api.v1.schemas.auth import SendOtpRequest
from app.services.send_message_serice import send_otp_sms
from utils.generate_otp import generate_otp
from utils.store_otp import store_otp



router = APIRouter()

@router.post("/send-otp")
async def send_otp(payload: SendOtpRequest):
    phone_number = payload.phone_number

    otp = generate_otp()

    store_otp['phone_number'] = phone_number
    store_otp['otp'] = otp
    store_otp['create_at'] = datetime.now().isoformat()


    is_success = send_otp_sms(phone_number=phone_number,otp=otp)
    print(is_success)
    if is_success:
        return {"message": "OTP sent successfully"}
    
    return {"message": "something went wrong"}