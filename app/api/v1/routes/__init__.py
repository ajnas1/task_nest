

from fastapi import APIRouter
from .auth.send_otp  import router  as send_otp_router


router = APIRouter()

router.include_router(send_otp_router,prefix="/auth", tags=["Auth"])