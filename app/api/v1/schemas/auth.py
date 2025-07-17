
from pydantic import BaseModel


class SendOtpRequest(BaseModel):
    phone_number: str
    