#!/usr/bin/env python

"""
Pandoc filter for converting horizontal rule to new page in LaTeX.
"""

from panflute import (
    HorizontalRule,
    MetaBool,
    MetaMap,
    RawBlock,
    run_filter,
)


def newpage(elem, doc):
    r"""
    Replace HorizontalRule by a \clearpage or a \cleardoublepage.

    Arguments
    ---------
    elem
        A pandoc element
    doc
        pandoc document

    Returns
    -------
        A RawBlock or None.
    """
    # Is it in the right format and is it an HorizontalRule?
    if doc.format == "latex" and isinstance(elem, HorizontalRule):
        if doc.double:
            return RawBlock("\\cleardoublepage", "tex")
        return RawBlock("\\clearpage", "tex")
    return None


def prepare(doc):
    """
    Prepare document.

    Arguments
    ---------
    doc
        pandoc document
    """
    doc.double = True

    if (
        "pandoc-latex-newpage" in doc.metadata.content
        and isinstance(doc.metadata.content["pandoc-latex-newpage"], MetaMap)
        and "double" in doc.metadata.content["pandoc-latex-newpage"]
        and isinstance(doc.metadata.content["pandoc-latex-newpage"]["double"], MetaBool)
    ):
        doc.double = doc.metadata.content["pandoc-latex-newpage"]["double"].boolean


def main(doc=None):
    """
    Convert the pandoc document.

    Arguments
    ---------
    doc
        pandoc document

    Returns
    -------
        The modified document.
    """
    return run_filter(newpage, prepare=prepare, doc=doc)


if __name__ == "__main__":
    main()
