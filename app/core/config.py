import os
from dotenv import load_dotenv

load_dotenv()
# Configuration settings for the application
# Ensure these environment variables are set in your .env file
DATABASE_URL = os.getenv("DATABASE_URL")