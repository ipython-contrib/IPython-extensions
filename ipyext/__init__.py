# coding: utf-8
from __future__ import absolute_import

from .inactive import InactiveMagics
from .writeandexecute import WriteAndExecuteMagics

all_class_magics = [InactiveMagics, WriteAndExecuteMagics]