

from pathlib import Path
from twilio.rest import Client
import os
from dotenv import load_dotenv


load_dotenv()
def send_otp_sms(phone_number: str,otp: str) -> bool:
    try:
        account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        client_phone = os.getenv("TWILIO_PHONE_NUMBER")

        if not all([account_sid, auth_token, client_phone]):
            raise ValueError("Missing Twilio credentials in environment variables.")
        
        client = Client(account_sid, auth_token)
        

        print("SID:", account_sid)
        print("TOKEN:", auth_token)
        print("FROM:", client_phone)

        message = client.messages.create(
        body=f"Your OTP is {otp}. Do not share it with anyone.",
        from_=client_phone,
        to=phone_number,
        )
        print(f"OTP {otp} sent to {phone_number}")
        return True
    except Exception  as e:
        print(e)
        return False