# validator.py
from utils import calculate_check_digit_10, calculate_check_digit_13
from messages import *

def validate_isbn_input(user_input: str):
    """Returns (is_valid: bool, message: str)"""
    user_input = user_input.strip()

    # Test 6 & 17
    if ',' not in user_input or len(user_input.split(',')) != 2:
        return False, ENTER_COMMA

    isbn_part, length_part = [p.strip() for p in user_input.split(',', 1)]

    # Test 7 & 16
    if not length_part.isdigit():
        return False, LENGTH_NOT_NUMBER

    length = int(length_part)
    if length not in (10, 13):
        return False, INVALID_LENGTH

    # Clean ISBN but keep original for character check
    clean_isbn = isbn_part.replace('-', '').replace(' ', '')
    
    if len(clean_isbn) != length:
        return False, WRONG_LENGTH.format(length=length)

    # Check for any invalid character (including letters, symbols, etc.)
    allowed = set('0123456789X- ')  # X only allowed at end for ISBN-10
    if not all(c in allowed for c in isbn_part):
        return False, INVALID_CHAR

    # Final strict check
    if length == 10:
        if not (clean_isbn[:-1].isdigit() and (clean_isbn[-1].isdigit() or clean_isbn[-1].upper() == 'X')):
            return False, INVALID_CHAR
    else:
        if not clean_isbn.isdigit():
            return False, INVALID_CHAR

    digits = [int(d) for d in clean_isbn[:-1]]
    given = clean_isbn[-1].upper()
    expected = calculate_check_digit_10(digits) if length == 10 else calculate_check_digit_13(digits)

    if given == expected:
        return True, VALID
    else:
        return False, INVALID
