import random


def generate_custom_phone_number():
    area_code = random.randint(100, 999)
    central_office_code = random.randint(100, 999)
    line_number = random.randint(1000, 9999)
    return f"({area_code})-{central_office_code}-{line_number}"