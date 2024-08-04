from unittest import TestCase
from panflute import convert_text

import pandoc_latex_newpage


class NewPageTest(TestCase):
    def verify_conversion(
        self,
        text,
        expected,
        transform,
        input_format="markdown",
        output_format="latex",
        standalone=False,
    ) -> None:
        """
        Verify the conversion.

        Parameters
        ----------
        text
            input text
        expected
            expected text
        transform
            filter function
        input_format
            input format
        output_format
            output format
        standalone
            is the output format standalone ?
        """
        doc = convert_text(text, input_format=input_format, standalone=True)
        doc.format = output_format
        doc = transform(doc)
        converted = convert_text(
            doc.content,
            input_format="panflute",
            output_format=output_format,
            extra_args=["--wrap=none"],
            standalone=standalone,
        )
        self.assertEqual(converted.strip(), expected.strip())

    def test_newpage(self):
        self.verify_conversion(
            """
Example

-------------

Example
            """,
            """
Example

\\cleardoublepage

Example
            """,
            pandoc_latex_newpage.main,
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

\\clearpage

Example
            """,
            pandoc_latex_newpage.main,
        )
