#Contains unit tests for the functions in password.py, such as verifying that passwords 
# are hashed correctly and that the validation function works as expected with 
# correct and incorrect passwords.



import unittest
from auth import set_password, validate_password, is_strong_password

class TestPasswordFunctions(unittest.TestCase):
    
    def test_set_password_hashing(self):
        """
        Test that set_password correctly hashes a plain-text password.
        """
        plain_password = "SecurePassword123!"
        hashed_password = set_password(plain_password)
        
        # Check that the hashed password is a byte string and not the same as the plain password
        self.assertIsInstance(hashed_password, bytes)
        self.assertNotEqual(plain_password.encode('utf-8'), hashed_password)

    def test_validate_password_correct(self):
        """
        Test that validate_password returns True for correct password.
        """
        plain_password = "SecurePassword123!"
        hashed_password = set_password(plain_password)
        
        # Check that validate_password returns True for the correct password
        self.assertTrue(validate_password(plain_password, hashed_password))

    def test_validate_password_incorrect(self):
        """
        Test that validate_password returns False for an incorrect password.
        """
        plain_password = "SecurePassword123!"
        wrong_password = "WrongPassword123!"
        hashed_password = set_password(plain_password)
        
        # Check that validate_password returns False for the incorrect password
        self.assertFalse(validate_password(wrong_password, hashed_password))

    def test_is_strong_password(self):
        """
        Test that is_strong_password correctly identifies strong passwords.
        """
        strong_password = "StrongPass123!"
        
        # Check that the strong password returns True
        self.assertTrue(is_strong_password(strong_password))

    def test_is_weak_password(self):
        """
        Test that is_strong_password identifies weak passwords.
        """
        weak_passwords = ["short", "alllowercase", "123456789", "NoSpecialChar123"]
        
        # Check that each weak password returns False
        for weak_password in weak_passwords:
            self.assertFalse(is_strong_password(weak_password))

if __name__ == '__main__':
    unittest.main()
