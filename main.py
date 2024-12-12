#Provides a basic example of how to use the library by integrating password and OTP 
# authentication functions. This file demonstrates the flow of a user logging in wit
# h password verification, OTP generation, and validation.

# main.py

from auth import (
    set_password, 
    validate_password, 
    is_strong_password, 
    generate_secret_key, 
    generate_otp, 
    validate_otp, 
    generate_qr_code_uri
)

def main():
    print("Welcome to the Virtual ID Authentication Library Demo")
    
    # Password Setup and Validation
    print("\n--- Password Setup and Validation ---")
    password = input("Enter a new password: ")

    # Check password strength
    if not is_strong_password(password):
        print("The password is weak. Ensure it meets the strength requirements.")
        return
    print("Password is strong!")

    # Hash the password
    hashed_password = set_password(password)
    print(f"Hashed Password: {hashed_password}")

    # Verify the password
    password_to_validate = input("Enter the password again to validate: ")
    if validate_password(password_to_validate, hashed_password):
        print("Password validation successful.")
    else:
        print("Password validation failed.")
        return

    # OTP Generation and Validation
    print("\n--- OTP Generation and Validation ---")
    secret_key = generate_secret_key()
    print(f"Secret Key: {secret_key}")

    # Generate an OTP
    otp = generate_otp(secret_key)
    print(f"Generated OTP: {otp}")

    # Prompt user to enter OTP for validation
    otp_to_validate = input("Enter the OTP to validate: ")
    if validate_otp(otp_to_validate, secret_key):
        print("OTP validation successful.")
    else:
        print("OTP validation failed.")

    # QR Code URI Generation (for Authenticator apps)
    print("\n--- Generate QR Code URI ---")
    account_name = input("Enter your account name (e.g., email): ")
    issuer_name = input("Enter the name of the service (e.g., MyApp): ")
    
    qr_code_uri = generate_qr_code_uri(secret_key, account_name, issuer_name)
    print(f"QR Code URI (for authenticator app): {qr_code_uri}")

    print("\nDemo Complete. Thank you for using the Virtual ID Authentication Library.")

if __name__ == "__main__":
    main()
