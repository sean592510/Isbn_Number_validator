#!/usr/bin/env python3
"""
ISBN-10 and ISBN-13 Validator
Supports hyphens, spaces, and 'X' check digit
"""

def calculate_check_digit_10(digits):
    """Calculate ISBN-10 check digit from first 9 digits"""
    total = sum(digit * (10 - i) for i, digit in enumerate(digits))
    result = (11 - (total % 11)) % 11
    return 'X' if result == 10 else str(result)


def calculate_check_digit_13(digits):
    """Calculate ISBN-13 check digit from first 12 digits"""
    total = sum(digit * (1 if i % 2 == 0 else 3) for i, digit in enumerate(digits))
    result = (10 - (total % 10)) % 10
    return str(result)


def validate_isbn(isbn: str, length: int = None) -> bool:
    """
    Validate ISBN-10 or ISBN-13
    Automatically detects length if not provided
    """
    # Clean input
    isbn = isbn.replace('-', '').replace(' ', '').upper()
    
    if length is None:
        if len(isbn) == 10:
            length = 10
        elif len(isbn) == 13:
            length = 13
        else:
            print(f"Invalid length: {len(isbn)} digits. Must be 10 or 13.")
            return False
    else:
        if len(isbn) != length:
            print(f"ISBN-{length} must have exactly {length} characters.")
            return False

    # Validate characters
    if length == 10:
        if not (isbn[:-1].isdigit() and (isbn[-1].isdigit() or isbn[-1] == 'X')):
            print("ISBN-10 contains invalid characters.")
            return False
    else:  # ISBN-13
        if not isbn.isdigit():
            print("ISBN-13 must contain only digits.")
            return False

    main_digits = [int(d) for d in isbn[:-1]]
    given_check = isbn[-1]

    expected_check = (
        calculate_check_digit_10(main_digits) if length == 10
        else calculate_check_digit_13(main_digits)
    )

    is_valid = str(given_check) == str(expected_check)
    
    if is_valid:
        print(f"Valid ISBN-{length}: {isbn}")
    else:
        print(f"Invalid ISBN-{length}")
        print(f"   Expected check digit: {expected_check} (got {given_check})")
    
    return is_valid


def main():
    print("ISBN Validator (supports ISBN-10 and ISBN-13)")
    print("Enter 'quit' to exit\n")
    
    while True:
        user_input = input("Enter ISBN (or 'quit'): ").strip()
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("Goodbye!")
            break
        if not user_input:
            continue
        validate_isbn(user_input)


if __name__ == "__main__":
    main()
