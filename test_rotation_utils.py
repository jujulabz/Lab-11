"""Lab-11 Unit testing
Melisa Palmer
Applying the fundementals of unit testing using the pytest library
Starter code 
4/5/2026"""

import pytest
from rotation_utils import adjust_rotation

def test_adjust_rotation_positive_within_range():
    """Test that a positive angle within 0-359 range returns unchanged."""
    assert adjust_rotation(100) == 100


def test_adjust_rotation_positive_single_overflow():
    """Test that 460 degrees wraps to 100 degrees."""
    assert adjust_rotation(460) == 100


def test_adjust_rotation_positive_double_overflow():
    """Test that 820 degrees (2+ rotations) wraps to 100 degrees."""
    assert adjust_rotation(820) == 100


def test_adjust_rotation_negative_within_range():
    """Test that -100 degrees converts to equivalent positive angle 260."""
    assert adjust_rotation(-100) == 260


d


