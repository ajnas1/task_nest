import os
from dotenv import load_dotenv

load_dotenv()
# Configuration settings for the application
# Ensure these environment variables are set in your .env file
DATABASE_URL = os.getenv("DATABASE_URL")



ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
CLIENT_PHONE = os.getenv("TWILIO_PHONE_NUMBER")