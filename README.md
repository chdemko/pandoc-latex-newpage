Installation
============

[![Python package](https://github.com/chdemko/pandoc-latex-newpage/workflows/Python%20package/badge.svg?branch=develop)](https://github.com/chdemko/pandoc-latex-newpage/actions/workflows/python-package.yml)
[![Hatch project](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://pypi.org/project/black/)
[![Coveralls](https://img.shields.io/coveralls/github/chdemko/pandoc-latex-newpage/develop.svg?logo=Codecov&logoColor=white)](https://coveralls.io/github/chdemko/pandoc-latex-newpage?branch=develop)
[![Scrutinizer](https://img.shields.io/scrutinizer/g/chdemko/pandoc-latex-newpage.svg?logo=scrutinizer)](https://scrutinizer-ci.com/g/chdemko/pandoc-latex-newpage/)
[![Code Climate](https://codeclimate.com/github/chdemko/pandoc-latex-newpage/badges/gpa.svg)](https://codeclimate.com/github/chdemko/pandoc-latex-newpage/)
[![CodeFactor](https://img.shields.io/codefactor/grade/github/chdemko/pandoc-latex-newpage/develop.svg?logo=codefactor)](https://www.codefactor.io/repository/github/chdemko/pandoc-latex-newpage)
[![Codacy](https://img.shields.io/codacy/grade/c831c2050ef64ed590bf0b37d204cd96.svg?logo=codacy)](https://app.codacy.com/gh/chdemko/pandoc-latex-newpage/dashboard)
[![PyPI version](https://img.shields.io/pypi/v/pandoc-latex-newpage.svg?logo=pypi&logoColor=white)](https://pypi.org/project/pandoc-latex-newpage/)
[![PyPI format](https://img.shields.io/pypi/format/pandoc-latex-newpage.svg?logo=pypi&logoColor=white)](https://pypi.org/project/pandoc-latex-newpage/)
[![License](https://img.shields.io/pypi/l/pandoc-latex-newpage.svg?logo=pypi&logoColor=white)](https://raw.githubusercontent.com/chdemko/pandoc-latex-newpage/develop/LICENSE)
[![Downloads](https://img.shields.io/pypi/dm/pandoc-latex-newpage?logo=pypi&logoColor=white)](https://pepy.tech/project/pandoc-latex-newpage)
[![Development Status](https://img.shields.io/pypi/status/pandoc-latex-newpage.svg?logo=pypi&logoColor=white)](https://pypi.org/project/pandoc-latex-newpage/)
[![Python version](https://img.shields.io/pypi/pyversions/pandoc-latex-newpage.svg?logo=Python&logoColor=white)](https://pypi.org/project/pandoc-latex-newpage/)
[![Pandoc version](https://img.shields.io/badge/pandoc-2.11%20|%202.12%20|%202.13%20|%202.14%20|%202.15%20|%202.16%20|%202.17%20|%202.18%20|%202.19%20|%203.0%20|%203.1%20|%203.2%20|%203.3%20|%203.4%20|%203.5-blue.svg?logo=markdown)](https://pandoc.org/)
[![Latest release](https://img.shields.io/github/release-date/chdemko/pandoc-latex-newpage.svg?logo=github)](https://github.com/chdemko/pandoc-latex-newpage/releases)
[![Last commit](https://img.shields.io/github/last-commit/chdemko/pandoc-latex-newpage/develop?logo=github)](https://github.com/chdemko/pandoc-latex-newpage/commit/develop/)
[![Repo Size](https://img.shields.io/github/repo-size/chdemko/pandoc-latex-newpage.svg?logo=github)](http://pandoc-latex-newpage.readthedocs.io/en/latest/)
[![Code Size](https://img.shields.io/github/languages/code-size/chdemko/pandoc-latex-newpage.svg?logo=github)](http://pandoc-latex-newpage.readthedocs.io/en/latest/)
[![Source Rank](https://img.shields.io/librariesio/sourcerank/pypi/pandoc-latex-newpage.svg?logo=libraries.io&logoColor=white)](https://libraries.io/pypi/pandoc-latex-newpage)
[![Docs](https://img.shields.io/readthedocs/pandoc-latex-newpage.svg?logo=read-the-docs&logoColor=white)](https://pandoc-latex-newpage.readthedocs.io)

*pandoc-latex-newpage* is a [pandoc] filter for converting horizontal
rule to new page in *LaTeX*.

[pandoc]: http://pandoc.org/

Instructions
------------

*pandoc-latex-newpage* requires [python], a programming language that comes
pre-installed on linux and Mac OS X, and which is easily installed
[on Windows]

Install *pandoc-latex-newpage* using the bash command

~~~shell-session
$ pipx install pandoc-latex-newpage
~~~

To upgrade to the most recent release, use

~~~shell-session
$ pipx upgrade pandoc-latex-newpage
~~~

`pipx` is a script to install and run python applications in isolated
environments from the Python Package Index, [PyPI]. It can be installed
using instructions given [here](https://pipx.pypa.io/stable/).

[python]: https://www.python.org
[on Windows]: https://www.python.org/downloads/windows
[PyPI]: https://pypi.org


Getting Help
------------

If you have any difficulties with *pandoc-latex-newpage*, please feel
welcome to [file an issue] on github so that we can help.

[file an issue]: https://github.com/chdemko/pandoc-latex-newpage/issues

Contribute
==========

Instructions
------------

Install `hatch`, then run

~~~shell-session
$ hatch run pip install pre-commit
$ hatch run pre-commit install
~~~

to install `pre-commit` before working on your changes.

Tests
-----

When your changes are ready, run

~~~shell-session
$ hatch test
$ hatch fmt --check
$ hatch run lint:check
$ hatch run docs:build
$ hatch build -t wheel
~~~

for running the tests, checking the style, building the documentation
and building the wheel.

