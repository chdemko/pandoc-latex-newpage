#!/usr/bin/env python

"""
Pandoc filter for converting horizontal rule to new page in LaTeX
"""

from panflute import HorizontalRule, RawBlock, run_filter  # type: ignore


def newpage(elem, doc):
    """
    Replace HorizontalRule by a \\cleardoublepage.
    """
    # Is it in the right format and is it an HorizontalRule?
    if doc.format == "latex" and isinstance(elem, HorizontalRule):
        return RawBlock("\\cleardoublepage", "tex")
    return None


def main(doc=None):
    """
    main function
    """
    return run_filter(newpage, doc=doc)


if __name__ == "__main__":
    main()
