# OTP Authentication Library

This project is a Python library designed to facilitate One-Time Password (OTP) authentication, password hashing, and validation. The library is lightweight, secure, and easy to integrate into your applications.

## Features

- **OTP Authentication**

  - Generate time-based OTPs using the `pyotp` library.
  - Validate OTPs securely.
  - Generate QR code URIs for easy integration with authenticator apps like Google Authenticator.

- **Password Management**

  - Hash and securely store passwords using `bcrypt`.
  - Validate passwords against stored hashes.
  - Ensure password strength with configurable requirements.

- **Comprehensive Unit Tests**

  - Automated tests for OTP generation, validation, and password management ensure robustness and reliability.

## Installation

Clone this repository and install the dependencies:

```bash
# Clone the repository
git clone https://github.com/merber520/mfa_library_v2.git

# Navigate to the project directory
cd otp_library

# Install required dependencies
pip install -r requirements.txt

# To run the demo, execute the main.py file
python main.py

#To run the fastapi server, execute the server/main.py
uvicorn Server.main:app --reload
```

## Usage

The main.py file is a demo for the usage of this library and could be a great start point for the user.


### Generating a QR Code URI

```python
from auth.otp import generate_qr_code_uri

# Generate a QR code URI for an authenticator app
qr_code_uri = generate_qr_code_uri(
    secret_key="BASE32SECRETKEY",
    account_name="user@example.com",
    issuer_name="MyApp"
)
print(qr_code_uri)
```

### Password Management

```python
from auth.password import set_password, validate_password, is_strong_password

# Hash a password
hashed_password = set_password("MySecurePassword123!")

# Validate a password
is_valid = validate_password("MySecurePassword123!", hashed_password)
print(f"Password is valid: {is_valid}")

# Check password strength
is_strong = is_strong_password("MySecurePassword123!")
print(f"Password is strong: {is_strong}")
```

## Running Tests

The project includes unit tests to verify functionality. Run the tests using:

```bash
pytest
```

## Dependencies

- `pyotp` - For OTP generation and validation.
- `bcrypt` - For secure password hashing.
- `pytest` - For running unit tests.

## Contribution

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
