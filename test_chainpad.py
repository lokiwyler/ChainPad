# test_chainpad.py
"""
Tests for ChainPad module.
"""

import unittest
from chainpad import ChainPad

class TestChainPad(unittest.TestCase):
    """Test cases for ChainPad class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ChainPad()
        self.assertIsInstance(instance, ChainPad)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ChainPad()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
