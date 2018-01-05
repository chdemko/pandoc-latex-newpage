# This Python file uses the following encoding: utf-8

from unittest import TestCase
from panflute import *

import pandoc_latex_newpage
from helper import verify_conversion

def test_newpage():
    verify_conversion(
        '''
Example

-------------

Example
        ''',
        '''
Example

\\cleardoublepage
Example
        ''',
        'latex'
    )

