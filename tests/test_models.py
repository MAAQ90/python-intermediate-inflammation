"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt

from inflammation.models import daily_mean, daily_max, daily_min

def test_daily_mean_zeros():
    """Test that mean function works for an array of zeros."""
    

    test_input = np.array([[0, 0],
                           [0, 0],
                           [0, 0]])
    test_result = np.array([0, 0])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)


def test_daily_mean_integers():
    """Test that mean function works for an array of positive integers."""

    test_input = np.array([[1, 2],
                           [3, 4],
                           [5, 6]])
    test_result = np.array([3, 4])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)

def test_daily_max_integers():
    
    test_input = np.array([[1, 2, 10],
                           [3, 40, 12],
                           [5, 6, 13]])
    test_result = np.array([5, 40, 13])

    npt.assert_array_equal(daily_max(test_input), test_result)


def test_daily_min_integers(): 
    
    test_daily_min_integers = np.array([[1, 2, 9],
                                        [3, 4, 1],
                                        [5, 6, 8]])
    test_result = np.array([1, 2, 1]) 

    npt.assert_array_equal(daily_min(test_daily_min_integers), test_result)

import pytest
from inflammation.models import daily_min
...
def test_daily_min_string():
    """Test for TypeError when passing strings"""

    with pytest.raises(TypeError): #Try ValueError
        error_expected = daily_min([['Hello', 'there'], ['General', 'Kenobi']])


