# This Python file uses the following encoding: utf-8

from unittest import TestCase
from panflute import convert_text

import pandoc_latex_newpage


class NewPageTest(TestCase):
    def verify_conversion(self, markdown, expected, format="markdown"):
        doc = convert_text(markdown, standalone=True)
        doc.format = format
        pandoc_latex_newpage.main(doc)
        converted = convert_text(
            doc.content,
            input_format="panflute",
            output_format="markdown",
            extra_args=["--wrap=none"],
            standalone=True,
        )
        self.assertEqual(converted, expected.strip())

    def test_newpage(self):
        self.verify_conversion(
            """
Example

-------------

Example
            """,
            """
Example

```{=tex}
\\cleardoublepage
```
Example
            """,
            "latex",
        )

    def test_newpage_single(self):
        self.verify_conversion(
            """
---
pandoc-latex-newpage:
  double: false
---

Example

-------------

Example
            """,
            """
Example

```{=tex}
\\clearpage
```
Example
            """,
            "latex",
        )
