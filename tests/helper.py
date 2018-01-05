# This Python file uses the following encoding: utf-8

from panflute import *

import pandoc_latex_newpage

def verify_conversion(markdown, expected, format='markdown'):
    doc = convert_text(markdown, standalone = True)
    doc.format = format
    pandoc_latex_newpage.main(doc)
    converted = convert_text(doc.content, input_format='panflute', output_format='markdown', extra_args=['--wrap=none'], standalone=True)
    assert converted == expected.strip()

