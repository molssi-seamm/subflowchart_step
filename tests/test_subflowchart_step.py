#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `subflowchart_step` package."""

import pytest  # noqa: F401
import subflowchart_step  # noqa: F401


def test_construction():
    """Just create an object and test its type."""
    result = subflowchart_step.Subflowchart()
    assert str(type(result)) == "<class 'subflowchart_step.subflowchart.Subflowchart'>"
