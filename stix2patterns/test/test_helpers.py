"""
Test cases for stix2patterns/helpers.py.
"""

from stix2patterns.helpers import leading_characters


def test_leading_characters():

    assert leading_characters('[file:size = 1280]', 2) == '[f'
    assert leading_characters(' [file:size = 1280]', 2) == '[f'
    assert leading_characters('( [file:size = 1280])', 2) == '(['
    assert leading_characters('[', 2) == '['
    assert leading_characters(None, 2) is None
