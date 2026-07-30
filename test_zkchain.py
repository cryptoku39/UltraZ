# test_zkchain.py
"""
Tests for ZKChain module.
"""

import unittest
from zkchain import ZKChain

class TestZKChain(unittest.TestCase):
    """Test cases for ZKChain class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ZKChain()
        self.assertIsInstance(instance, ZKChain)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ZKChain()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
