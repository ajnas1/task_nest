from random import randint


def generate_otp() -> int:
    otp = randint(1000,9999)
    return otp