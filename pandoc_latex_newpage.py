#!/usr/bin/env python

"""
Pandoc filter for converting horizontal rule to new page in LaTeX
"""

from panflute import *

def newpage(elem, doc):
    # Is it in the right format and is it an HorizontalRule?
    if doc.format == 'latex' and isinstance(elem, HorizontalRule):
        return RawBlock('\\cleardoublepage', 'tex')

def main(doc = None):
    return run_filter(newpage, doc = doc)

if __name__ == '__main__':
    main()

