Usage
=====

To apply the filter, use the following option with pandoc:

~~~shell
$ pandoc --filter pandoc-latex-newpage
~~~

Explanation
-----------

All horizontal rules will be replaced by a new page
(a `\clearpage` or a `\cleardoublepage` command in LaTeX)

Example
-------

Demonstration: Using [pandoc-latex-newpage-sample.txt] as input gives output
file in [pdf].

[pandoc-latex-newpage-sample.txt]: https://raw.githubusercontent.com/chdemko/pandoc-latex-newpage/develop/docs/images/pandoc-latex-newpage-sample.txt
[pdf]: https://raw.githubusercontent.com/chdemko/pandoc-latex-newpage/develop/docs/images/pandoc-latex-newpage-sample.pdf
