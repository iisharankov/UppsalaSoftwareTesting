# By Jyong-Jhih Lin
# Software Testing Project 2021 Aumumn period 2: itertools, python=3.9.7
# count(), whitebox


from itertools import count
import pytest
import sys
import decimal


# check prime path [1,2,3,2,3] for whitebox testing
def test_count_normal():
    test = count(start=0, step=1)
    assert next(test) == 0
    assert next(test) == 1