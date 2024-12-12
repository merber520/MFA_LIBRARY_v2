

import pyotp

def generate_secret_key() -> str:
    """
    Generates a new base32 encoded secret key for OTP.
    
    Returns:
        str: A base32 encoded secret key for use in TOTP generation.
    """
    
    return pyotp.random_base32()


def generate_otp(secret_key: str) -> str:
    """
    Generates a time-based OTP using the provided secret key.
    
    Args:
        secret_key (str): The base32 encoded secret key for generating the OTP.
        
    Returns:
        str: A 6-digit OTP as a string.
    """
    
    totp = pyotp.TOTP(secret_key)
    return totp.now()


def validate_otp(otp: str, secret_key: str) -> bool:
    """
    Validates the provided OTP against the expected OTP generated with the secret key.
    
    Args:
        otp (str): The OTP to be validated.
        secret_key (str): The base32 encoded secret key for validating the OTP.
        
    Returns:
        bool: True if the OTP is valid, False otherwise.
    """
    
    # Initialize TOTP with the provided secret key
    totp = pyotp.TOTP(secret_key)
    # Verify the provided OTP against the current TOTP
    return totp.verify(otp)


def generate_qr_code_uri(secret_key: str, account_name: str, issuer_name: str) -> str:
    """
    Generates a URI for a QR code that can be used to add the OTP setup in an authenticator app.
    
    Args:
        secret_key (str): The base32 encoded secret key for the OTP.
        account_name (str): The account name for which the OTP is being set up (e.g., user email).
        issuer_name (str): The name of the organization or app (e.g., "MyApp").
        
    Returns:
        str: A URI that can be converted into a QR code.
    """
    
    totp = pyotp.TOTP(secret_key)
    return totp.provisioning_uri(name=account_name, issuer_name=issuer_name)
