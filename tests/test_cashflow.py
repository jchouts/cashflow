#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_cashflow
----------------------------------

Tests for `cashflow` module.
"""
import pytest

from cashflow import cashflow


pytest.fixture(params=[1,2])
def sample_fixture(request):
    return request.param

def test_sample(sample_fixture):
    assert sample_fixture in [1,2,3,4,5]


