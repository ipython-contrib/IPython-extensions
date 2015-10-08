# -*- coding: utf-8 -*-
"""Tests for various magic functions.
Needs to be run by nose (to make ipython session available).
"""

from __future__ import absolute_import

import io
import os
import sys
import warnings
from unittest import TestCase, skipIf

try:
    from importlib import invalidate_caches   # Required from Python 3.3
except ImportError:
    def invalidate_caches():
        pass

import nose.tools as nt

from IPython import get_ipython
from IPython.testing import tools as tt
from IPython.utils import py3compat
from IPython.utils.io import capture_output


def test_time():
    ip = get_ipython() 
    
    with tt.AssertPrints("'inactive' magic loaded"):
        ip.run_cell("%reload_ext ipyext.inactive")
    
    with tt.AssertPrints("Cell inactive: not executed!"):
        with tt.AssertNotPrints("code not run", suppress=False):
            ip.run_cell("%%inactive\nprint('code not run...')")