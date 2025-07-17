

from pathlib import Path
from twilio.rest import Client
import os
from dotenv import load_dotenv

from app.core.config import ACCOUNT_SID, AUTH_TOKEN, CLIENT_PHONE


def send_otp_sms(phone_number: str,otp: str) -> bool:
    try:
        
        if not all([ACCOUNT_SID, AUTH_TOKEN, CLIENT_PHONE]):
            raise ValueError("Missing Twilio credentials in environment variables.")
        
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        

        print("SID:", ACCOUNT_SID)
        print("TOKEN:", AUTH_TOKEN)
        print("FROM:", CLIENT_PHONE)

        message = client.messages.create(
        body=f"Your OTP is {otp}. Do not share it with anyone.",
        from_=CLIENT_PHONE,
        to=phone_number,
        )
        print(f"OTP {otp} sent to {phone_number}")
        return True
    except Exception  as e:
        print(e)
        return False