"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest

from inflammation.models import daily_mean, daily_max, daily_min

@pytest.mark.parametrize(
    "test, expected",
    [
        ([ [0, 0], [0, 0], [0, 0] ], [0, 0]),
        ([ [1, 2], [3, 4], [5, 6] ], [3, 4]),
    ])

def test_daily_mean(test, expected):
    """Test mean function works for array of zeroes and positive integers."""
    npt.assert_array_equal(daily_mean(np.array(test)), np.array(expected))

@pytest.mark.parametrize(
"testMAX, expectedMAX",
[
    ([[1, 2, 10], [3, 40, 12], [5, 6, 13]], [5, 40, 13])
])

def test_daily_max(testMAX, expectedMAX):
    
    #test_input = np.array([[1, 2, 10],
    #                       [3, 40, 12],
    #                       [5, 6, 13]])
    #test_result = np.array([5, 40, 13])

    #npt.assert_array_equal(daily_max(test_input), test_result)
    npt.assert_array_equal(daily_max(np.array(testMAX)), np.array(expectedMAX))



@pytest.mark.parametrize(
    "testMIN, expectedMIN",
    [
        ([[1, 2, 10], [3, 40, 12], [5, 6, 13]], [5, 40, 13])
    ]    
    )

def test_daily_min(testMIN, expectedMIN):
    
    #test_input = np.array([[1, 2, 10],
    #                       [3, 40, 12],
    #                       [5, 6, 13]])
    #test_result = np.array([5, 40, 13])

    #npt.assert_array_equal(daily_max(test_input), test_result)
    npt.assert_array_equal(daily_max(np.array(testMIN)), np.array(expectedMIN))
'''
def test_daily_min(): 
    
    test_daily_min = np.array([[1, 2, 9],
                                        [3, 4, 1],
                                        [5, 6, 8]])
    test_result = np.array([1, 2, 1]) 

    npt.assert_array_equal(daily_min(test_daily_min), test_result)'
'''

def test_daily_min_string():
    """Test for TypeError when passing strings"""

    with pytest.raises(TypeError): #Try ValueError
        error_expected = daily_min([['Hello', 'there'], ['General', 'Kenobi']])


