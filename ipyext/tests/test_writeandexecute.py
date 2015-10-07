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
from IPython.utils.tempdir import TemporaryDirectory

from IPython.core.error import UsageError

TF_NAME = "xxx_temp_foo.py"

def test_writeandexecute_basics():
    ip = get_ipython()

    with tt.AssertPrints("'writeandexecute' magic loaded"):
        ip.run_cell("%reload_ext ipyext.writeandexecute")


    with tt.AssertPrints("Hello world", suppress=False):
        ip.run_cell("%%writeandexecute -d -i bla xxx_temp_foo\nprint('Hello world')")
    
    with io.open(TF_NAME, 'r', encoding='utf-8') as tf:
        content = tf.read()
        nt.assert_in("# -*- coding: utf-8 -*-", content)
        nt.assert_in("# -- ==bla== --", content)
        nt.assert_in("print('Hello world')", content)
    os.unlink(TF_NAME)

def test_writeandexecute_userrrors():
    ip = get_ipython()

    with tt.AssertPrints("'writeandexecute' magic loaded"):
        ip.run_cell("%reload_ext ipyext.writeandexecute")

    # no content
    with tt.AssertNotPrints("Hello world"):
        with tt.AssertPrints("cell body is empty", channel='stderr'):
            ip.run_cell("%%writeandexecute -d -i bla xxx_temp_foo")

    with tt.AssertNotPrints("Hello world"):
        with tt.AssertPrints("cell body is empty", channel='stderr'):
            ip.run_cell("%%writeandexecute -d -i bla xxx_temp_foo\n")

    # no identifier
    with tt.AssertNotPrints("Hello world"):
        with tt.AssertPrints("Missing indentifier", channel='stderr'):
            ip.run_cell("%%writeandexecute xxx_temp_foo\nprint('Hello world')")

    # no filename
    with tt.AssertNotPrints("Hello world"):
        with tt.AssertPrints("Missing filename", channel='stderr'):
            ip.run_cell("%%writeandexecute -i bla\nprint('Hello world')")

    nt.assert_false(os.path.exists(TF_NAME))


def test_writeandexecute_content():
    ip = get_ipython()

    with tt.AssertPrints("'writeandexecute' magic loaded"):
        ip.run_cell("%reload_ext ipyext.writeandexecute")

    ip.run_cell("a = 0")

    with tt.make_tempfile(TF_NAME):

        # run something ones, to get the file setup
        with tt.AssertPrints("Hello world"):
            ip.run_cell("%%writeandexecute -i bla xxx_temp_foo\nprint('Hello world')")

        with io.open(TF_NAME, 'a', encoding='utf-8') as tf:
            tf.write(u"\n# -- ==blub== --\n")

        # only one identifier
        with tt.AssertPrints("Exception: Found only one line with identifier", suppress=False):
            ip.run_cell("%%writeandexecute -d -i blub xxx_temp_foo\nprint('Hello world1')\na=1")

        #This should not be executed...
        with tt.AssertPrints("a=0"):
            ip.run_cell("print('a=%s' % a)")

        with io.open(TF_NAME, 'a', encoding='utf-8') as tf:
            tf.write(u"\n# -- ==blub== --\n")

        # two should work
        with tt.AssertPrints("Hello world2", suppress=False):
            ip.run_cell("%%writeandexecute -d -i blub xxx_temp_foo\nprint('Hello world2')\na=2")

        with io.open(TF_NAME, 'a', encoding='utf-8') as tf:
            tf.write(u"\n# -- ==blub== --\n")

        # three is bad again identifier
        with tt.AssertPrints("Exception: Found more than two lines with identifier", suppress=False):
            ip.run_cell("%%writeandexecute -d -i blub xxx_temp_foo\nprint('Hello world3')\na=3")

        # make sure that only the second one got executed...
        with tt.AssertPrints("a=2"):
            ip.run_cell("print('a=%s' % a)")

        # make sure that only the second one got written to the file
        with io.open(TF_NAME, 'r', encoding='utf-8') as tf:
            content = tf.read()
            nt.assert_in("print('Hello world2')", content)
