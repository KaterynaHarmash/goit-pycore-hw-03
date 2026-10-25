import re

def normalize_phone(phone_number):
    """
    Normalize a phone number by removing any non-numeric characters
    and formatting it in a standard way.

    Args:
        phone_number (str): The phone number to normalize."""
    
    # Remove all non-numeric characters
    cleaned_number = re.sub('[^0-9+]', '', phone_number)
    if cleaned_number.startswith('+380'):
        pass  # Already in the correct format
    elif cleaned_number.startswith('380'):
        cleaned_number = '+' + cleaned_number
    elif cleaned_number.startswith('0'):
        cleaned_number = '+38' + cleaned_number
    else:
        cleaned_number = '+3' + cleaned_number

    return cleaned_number
   
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)