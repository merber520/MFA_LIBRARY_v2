#Initializes the auth module, allowing password.py and otp.py to be imported as part of 
# auth. This file can remain empty or include imports to expose specific functions from 
# password.py and otp.py.

# __init__.py

# Import functions from password.py
from .password import set_password, validate_password, is_strong_password

# Import functions from otp.py
from .otp import generate_secret_key, generate_otp, validate_otp, generate_qr_code_uri

# Define __all__ to specify the public interface of the module
__all__ = [
    "set_password",
    "validate_password",
    "is_strong_password",
    "generate_secret_key",
    "generate_otp",
    "validate_otp",
    "generate_qr_code_uri"
]
