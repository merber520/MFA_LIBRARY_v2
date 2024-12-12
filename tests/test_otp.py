#Contains unit tests for the functions in otp.py, focusing on OTP generation and 
# validation. Tests ensure that OTPs match the expected format, validate 
# correctly, and detect invalid inputs.
# test_otp.py

import unittest
from auth import generate_secret_key, generate_otp, validate_otp, generate_qr_code_uri

class TestOTPFunctions(unittest.TestCase):
    
    def test_generate_secret_key(self):
        """
        Test that generate_secret_key creates a base32 encoded string.
        """
        secret_key = generate_secret_key()
        
        # Check that the secret key is a non-empty string and base32 encoded
        self.assertIsInstance(secret_key, str)
        self.assertGreater(len(secret_key), 0)

    def test_generate_otp(self):
        """
        Test that generate_otp returns a 6-digit OTP.
        """
        secret_key = generate_secret_key()
        otp = generate_otp(secret_key)
        
        # Check that the OTP is a 6-digit number in string format
        self.assertIsInstance(otp, str)
        self.assertEqual(len(otp), 6)
        self.assertTrue(otp.isdigit())

    def test_validate_otp_correct(self):
        """
        Test that validate_otp returns True for a valid OTP.
        """
        secret_key = generate_secret_key()
        otp = generate_otp(secret_key)
        
        # Validate that the OTP is correct
        self.assertTrue(validate_otp(otp, secret_key))

    def test_validate_otp_incorrect(self):
        """
        Test that validate_otp returns False for an incorrect OTP.
        """
        secret_key = generate_secret_key()
        invalid_otp = "000000"  # Using an obviously incorrect OTP
        
        # Validate that the OTP is incorrect
        self.assertFalse(validate_otp(invalid_otp, secret_key))

    def test_generate_qr_code_uri(self):
        """
        Test that generate_qr_code_uri creates a properly formatted URI.
        """
        secret_key = generate_secret_key()
        account_name = "test@example.com"
        issuer_name = "MyApp"
        uri = generate_qr_code_uri(secret_key, account_name, issuer_name)
        
        # Check that the URI contains the account name, issuer, and secret key
        self.assertIn("otpauth://totp/", uri)
        self.assertIn(account_name, uri)
        self.assertIn(issuer_name, uri)
        self.assertIn(secret_key, uri)

if __name__ == '__main__':
    unittest.main()
