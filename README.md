# pandoc-latex-newpage
![Python package](https://github.com/chdemko/pandoc-latex-newpage/workflows/Python%20package/badge.svg?branch=develop)
[![Coveralls](https://img.shields.io/coveralls/github/chdemko/pandoc-latex-newpage/0.2.0.svg)](https://coveralls.io/github/chdemko/pandoc-latex-newpage?branch=0.2.0)
[![Scrutinizer](https://img.shields.io/scrutinizer/g/chdemko/pandoc-latex-newpage.svg)](https://scrutinizer-ci.com/g/chdemko/pandoc-latex-newpage/)
[![PyPI version](https://img.shields.io/pypi/v/pandoc-latex-newpage.svg)](https://pypi.org/project/pandoc-latex-newpage/)
[![PyPI format](https://img.shields.io/pypi/format/pandoc-latex-newpage.svg)](https://pypi.org/project/pandoc-latex-newpage/)
[![License](https://img.shields.io/pypi/l/pandoc-latex-newpage.svg)](https://raw.githubusercontent.com/chdemko/pandoc-latex-newpage/0.2.0/LICENSE)
[![Python version](https://img.shields.io/pypi/pyversions/pandoc-latex-newpage.svg)](https://pypi.org/project/pandoc-latex-newpage/)
[![Development Status](https://img.shields.io/pypi/status/pandoc-latex-newpage.svg)](https://pypi.org/project/pandoc-latex-newpage/)

*pandoc-latex-newpage* is a [pandoc] filter for converting horizontal rule to new page in *LaTeX*.

[pandoc]: http://pandoc.org/

Documentation
-------------

See the [wiki pages](https://github.com/chdemko/pandoc-latex-newpage/wiki).

Usage
-----

To apply the filter, use the following option with pandoc:

    --filter pandoc-latex-newpage

Installation
------------

*pandoc-latex-newpage* requires [python], a programming language that comes pre-installed on linux and Mac OS X, and which is easily installed [on Windows]. Either python 2.7 or 3.x will do.

Install *pandoc-latex-newpage* as root using the bash command

    pip install pandoc-latex-newpage

To upgrade to the most recent release, use

    pip install --upgrade pandoc-latex-newpage

To upgrade to the current code, use

    pip install --upgrade --force git+https://github.com/chdemko/pandoc-latex-newpage

`pip` is a script that downloads and installs modules from the Python Package Index, [PyPI].  It should come installed with your python distribution. If you are running linux, `pip` may be bundled separately. On a Debian-based system (including Ubuntu), you can install it as root using

    apt-get update
    apt-get install python-pip

[python]: https://www.python.org
[on Windows]: https://www.python.org/downloads/windows
[PyPI]: https://pypi.org


Getting Help
------------

If you have any difficulties with *pandoc-latex-newpage*, please feel welcome to [file an issue] on github so that we can help.

[file an issue]: https://github.com/chdemko/pandoc-latex-newpage/issues

