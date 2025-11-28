# utils.py
def calculate_check_digit_10(digits):
    total = sum(digit * (10 - i) for i, digit in enumerate(digits))
    result = (11 - total % 11) % 11
    return 'X' if result == 10 else str(result)

def calculate_check_digit_13(digits):
    total = sum(digit * (1 if i % 2 == 0 else 3) for i, digit in enumerate(digits))
    result = (10 - total % 10) % 10
    return str(result)
