#Contains functions for password management, specifically for hashing passwords
#ecurely and validating passwords during authentication.

# password.py

import bcrypt  # bcrypt for hashing and verifying passwords
import re

def set_password(password: str) -> bytes:
    """
    Hashes a plain-text password using bcrypt.
    
    Args:
        password (str): The plain-text password provided by the user.
        
    Returns:
        bytes: A bcrypt hashed version of the password, safe for storage.
    """
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


def validate_password(password: str, hashed_password: bytes) -> bool:
    """
    Validates a plain-text password against a hashed password.
    
    Args:
        password (str): The plain-text password to verify.
        hashed_password (bytes): The previously hashed password stored in the database.
        
    Returns:
        bool: True if the password is correct, False otherwise.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)


def is_strong_password(password: str) -> bool:
    """
    Checks if the password meets security standards (length, complexity).
    
    Args:
        password (str): The plain-text password to check.
        
    Returns:
        bool: True if the password meets security requirements, False otherwise.
    """
    # Define the password strength requirements
    min_length = 8
    has_uppercase = re.search(r"[A-Z]", password) is not None
    has_lowercase = re.search(r"[a-z]", password) is not None
    has_digit = re.search(r"\d", password) is not None
    has_special_char = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is not None

    # Check if the password meets all the criteria
    if (len(password) >= min_length and has_uppercase and has_lowercase
            and has_digit and has_special_char):
        return True
    return False
