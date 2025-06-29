"""
Basic unit tests for Campers Wallet application.
Demonstrates testing capabilities for core functionality.
"""

import unittest
import tempfile
import os
import json
from unittest.mock import patch, MagicMock
import sys
import config
from utils import (
    hash_password, verify_password, validate_email, 
    validate_password_strength, format_currency
)
import data


class TestUtils(unittest.TestCase):
    """Test cases for utility functions."""
    
    def test_hash_password(self):
        """Test password hashing functionality."""
        password = "TestPassword123"
        hashed = hash_password(password)
        
        # Hash should be different from original password
        self.assertNotEqual(password, hashed)
        
        # Hash should be consistent
        hashed2 = hash_password(password)
        self.assertEqual(hashed, hashed2)
    
    def test_verify_password(self):
        """Test password verification."""
        password = "TestPassword123"
        hashed = hash_password(password)
        
        # Correct password should verify
        self.assertTrue(verify_password(password, hashed))
        
        # Wrong password should not verify
        self.assertFalse(verify_password("WrongPassword", hashed))
    
    def test_validate_email(self):
        """Test email validation."""
        # Valid emails
        valid_emails = [
            "test@example.com",
            "user.name@domain.co.uk",
            "user+tag@example.org"
        ]
        
        for email in valid_emails:
            with self.subTest(email=email):
                self.assertTrue(validate_email(email))
        
        # Invalid emails
        invalid_emails = [
            "invalid-email",
            "@example.com",
            "user@",
            "user@.com"
        ]
        
        for email in invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(validate_email(email))
    
    def test_validate_password_strength(self):
        """Test password strength validation."""
        # Valid password
        valid_password = "StrongPass123"
        is_valid, error = validate_password_strength(valid_password)
        self.assertTrue(is_valid)
        self.assertEqual(error, "")
        
        # Too short
        short_password = "Short1"
        is_valid, error = validate_password_strength(short_password)
        self.assertFalse(is_valid)
        self.assertIn("caracteres", error)
        
        # No number
        no_number = "NoNumberPass"
        is_valid, error = validate_password_strength(no_number)
        self.assertFalse(is_valid)
        self.assertIn("número", error)
        
        # No uppercase
        no_upper = "noupperpass123"
        is_valid, error = validate_password_strength(no_upper)
        self.assertFalse(is_valid)
        self.assertIn("mayúscula", error)
        
        # No lowercase
        no_lower = "NOLOWERPASS123"
        is_valid, error = validate_password_strength(no_lower)
        self.assertFalse(is_valid)
        self.assertIn("minúscula", error)
    
    def test_format_currency(self):
        """Test currency formatting."""
        amount = 1234567.89
        
        # Default COP formatting
        formatted = format_currency(amount)
        self.assertEqual(formatted, "$1,234,567.89 COP")
        
        # USD formatting
        formatted_usd = format_currency(amount, "USD")
        self.assertEqual(formatted_usd, "$1,234,567.89 USD")
        
        # Zero amount
        formatted_zero = format_currency(0)
        self.assertEqual(formatted_zero, "$0.00 COP")


class TestDataHandling(unittest.TestCase):
    """Test cases for data handling functions."""
    
    def setUp(self):
        """Set up test environment."""
        self.test_data = {
            "user1": {"name": "Test User", "balance": 1000},
            "user2": {"name": "Another User", "balance": 500}
        }
    
    def test_validate_data(self):
        """Test data validation."""
        # Valid data
        self.assertTrue(data.validate_data(self.test_data))
        
        # Invalid data types
        self.assertFalse(data.validate_data("not a dict"))
        self.assertFalse(data.validate_data(123))
        self.assertFalse(data.validate_data([]))
    
    @patch('data.get_file_path')
    def test_load_data_file_not_found(self, mock_get_path):
        """Test loading data when file doesn't exist."""
        # Mock file path
        mock_path = MagicMock()
        mock_path.exists.return_value = False
        mock_get_path.return_value = mock_path
        
        # Should return empty dict
        result = data.load_data("users")
        self.assertEqual(result, {})
    
    @patch('data.get_file_path')
    def test_load_data_invalid_json(self, mock_get_path):
        """Test loading data with invalid JSON."""
        # Create temporary file with invalid JSON
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write("invalid json content")
            temp_file_path = temp_file.name
        
        try:
            # Mock file path
            mock_path = MagicMock()
            mock_path.exists.return_value = True
            mock_get_path.return_value = mock_path
            
            # Mock file reading
            with patch('builtins.open', create=True) as mock_open:
                mock_open.return_value.__enter__.return_value.read.return_value = "invalid json"
                
                # Should return empty dict
                result = data.load_data("users")
                self.assertEqual(result, {})
        finally:
            # Clean up
            os.unlink(temp_file_path)


class TestConfig(unittest.TestCase):
    """Test cases for configuration."""
    
    def test_config_constants(self):
        """Test configuration constants."""
        # Check that required constants exist
        self.assertTrue(hasattr(config, 'MIN_PASSWORD_LENGTH'))
        self.assertTrue(hasattr(config, 'MIN_AGE'))
        self.assertTrue(hasattr(config, 'MIN_NAME_LENGTH'))
        self.assertTrue(hasattr(config, 'SUPPORTED_CURRENCIES'))
        
        # Check values are reasonable
        self.assertGreater(config.MIN_PASSWORD_LENGTH, 0)
        self.assertGreater(config.MIN_AGE, 0)
        self.assertGreater(config.MIN_NAME_LENGTH, 0)
        self.assertIsInstance(config.SUPPORTED_CURRENCIES, list)
        self.assertGreater(len(config.SUPPORTED_CURRENCIES), 0)


def run_tests():
    """Run all tests and display results."""
    print("🧪 Ejecutando pruebas unitarias para Campers Wallet...")
    print("=" * 60)
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test cases
    suite.addTests(loader.loadTestsFromTestCase(TestUtils))
    suite.addTests(loader.loadTestsFromTestCase(TestDataHandling))
    suite.addTests(loader.loadTestsFromTestCase(TestConfig))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Display summary
    print("=" * 60)
    if result.wasSuccessful():
        print("✅ Todas las pruebas pasaron exitosamente!")
    else:
        print(f"❌ {len(result.failures)} pruebas fallaron")
        print(f"❌ {len(result.errors)} pruebas tuvieron errores")
    
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1) 