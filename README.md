# Installation

![Python package](https://github.com/chdemko/pandoc-latex-newpage/workflows/Python%20package/badge.svg?branch=develop)
[![Coveralls](https://img.shields.io/coveralls/github/chdemko/pandoc-latex-newpage/develop.svg?logo=Codecov&logoColor=white)](https://coveralls.io/github/chdemko/pandoc-latex-newpage?branch=develop)
[![Scrutinizer](https://img.shields.io/scrutinizer/g/chdemko/pandoc-latex-newpage.svg)](https://scrutinizer-ci.com/g/chdemko/pandoc-latex-newpage/)
[![PyPI version](https://img.shields.io/pypi/v/pandoc-latex-newpage.svg?logo=Python&logoColor=white)](https://pypi.org/project/pandoc-latex-newpage/)
[![PyPI format](https://img.shields.io/pypi/format/pandoc-latex-newpage.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIAAAACACAYAAADDPmHLAAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAA3XAAAN1wFCKJt4AAAAB3RJTUUH4gwPFiYw92eBNAAAAgJJREFUeNrt3T1WwkAUgNH31Br3ogWptdAlgyvQxYgHeh0LKKxI+PHAzNyvRo8xlxl5CZKllBIaax0Rr5n53tqB3Ti3k7qPiEUpZQAAggEACAYAIBgAgGAAoG8Ey9oRAHBas9oR5NgcIDOz5TN4pjnIJiJeapwTWAFGfMR2CDRlJViUUuYAtAfgOSK+Jv5N8FbddlBGav4M7+9795jHUsqqTGtdFQIAxgE0jQCAaQCaRQDAdABNIgDgMADNIQDgcAB/EHxWjwCA4wDsvvahegQAHA+gCQQAnAagegQAnA6gagQAnAdArQhcDdx//D+ZeXvg95tHxDK21wbG2mTm/SWP38Wgcz+jMj8i4ikiVhMePrv0z3vnlO1/grS+DVoBehfuVwCAABAAAkAAqLO6nwP896Tz2ucIVgBbgAAQAAJAAAgAASAABIAAEAACQAAIADXZyfcD9P55A7W/c8oKYAsQAAJAAAgAASBzgJ5eB1sBBIAAEAACQAAIAJkDTM/9AO4HEAACQAAIAAEgANTPHMD9AFYAASAABIAAEAACQP3MAWq/H6D3OYYVwBYgAASAABAAAkDmAF5HWwEEgAAQAAJAAAgAASAABIAAEAACQAAIAAEgAASAABAAAkAACAABIAAEgAAQAAJAAAgAXVWj/x+g988FtAIIAAEgAASAABAAaqhfB1BFkJjdTNQAAAAASUVORK5CYII=)](https://pypi.org/project/pandoc-latex-newpage/)
[![License](https://img.shields.io/pypi/l/pandoc-latex-newpage.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIAAAABmCAYAAAADI5lUAAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAA3XAAAN1wFCKJt4AAAAB3RJTUUH4gwPFiQKA106BAAABUNJREFUeNrtnV2IFlUYx3/P625qbrGlpWmWdaMVKau2EmpCrSDqxRpUUkr0SYVEFyFRUXQhfUAihTdCESVpKpKQpLZBsghltn605VVKpmZgGYvmbhpPFzMbWu3LO7szO1//H+zN7sw5c57nd8685+zMeY0quLsB04FW4A7gWmAMMAyRRbqBE8BRYCfwMfCNmXlfJ1iV5LcAbwBNimuu+Q54xcw21iSAuzcA7wOLFLtCsQl4yMxO9ymAu48HtgK3Kl6F5ACw0Mx++o8AYc/fBUxWnArN98DtZtYFULngDx8o+aXgZuDdi0YAd58fDv2iPMwzs+0WTvX2qfeXjv1Ak7n7DOBLxaOU3FYhWOQR5aS1AsxWHErLnArB8q4oJ+PM3buBoRFO6gJ2K3aZpBm4PMLxPXh09ijO2cTd90RNZkVhKzcSQAIICSAkgJAAQgIICSAkgJAAQgIICSAKT91gVOLui4EVKbZzvZm9kGD7rgHmEbw9NRoYCTQCvwInCd7UaQPaep/GLZUABP+ivDHFdo5KKPHTgNeAu6jyllXIk8A5d/8QeN7MjusWkGPcfRnBs5QtNSS/l3rgQaDT3e+UAPlN/iPA2wMYQa8APnH3ZgmQv+SPBlbGUNRw4D13r5MA+WIF0R67qsZNwMMSID+9vwF4IOZin5AA+WE+8W+O0eTuN0iAfNCSs3IlQMxMSqjciRIgH0wsmgCDNQU5CKxJMXHtMXwAHAJcndD1jSu0AGbWHkcSUmZEgmVfqltA9kkySQ0SIPsMyWnZEiAm/kiw7DMSIPt0AecSKvukBMg4ZvYXcCSh4g9LgHzwVc7KzcY00N0XAM+kmLitZrYqhnLagPsTuL7PCy0AwUJHS4oCHMpwok4AnboF5ONzwJFwFIiTd6pt5y4BssebMZbVA6xOszESIDrbiW+TrDVm9rMEyNdtwIHHgPMDLOoX4KW02yMB+ifBAWCgs4qnzex3CZBfXgS+7ee568xsQxYaIQH6Pwr0ELzk8WfEU48Dy7LSDgkwMAn2Eu2dRwceNbPfJEBxeD3s1bWwzcw+zdLFD9ZK4DHiX0CJwsEkbwXuvrrGkWBl5vTVXsGxxHBaDXE76+71CV+H9gpOiRM1HHPKzM5l7cIlQDxcX8Mxo9x9uAQoJktqOKYeuE8CFO/+P5NgabgWXnX3sRKgOMmfDWyJMJsaA+xw9wkSIN+Jr7j7U+HUdmTE028Bdrv73NKsA4Q9ZUmK7Ww3s7UxtaUZeAuYMYBirgpHgg3AcjP7sdACEOyE8XjKsq8dSI8H5gLPEu+jbfcCi9x9PbDKzDqKKkBeh/rpwN0Eu4Jcl1A19cBSYKm77wXWAZvN7AcJkG7ypwBfD3K1TeHPy+7eaGbnk65QHwL7ZlKKdY8AxmsWkC5XlqF+CdA3jWWoXwL0TUPK9V8mAdLlkpTrr5cA6VInAcpNfRnqHyzLu4jvBc3+0J8NGE6lfM1nB6UWPRJWHPRImNBnACEBhAQQEkBIACEBhAQQEkBIACEBhAQQ/8bcvRsYGuGcLuLbJ0/ESzPRvtW0x9z9MDBBsSslhyoE27eIcnKsAuxUHErLFxWC15tFOdli7m7AXmCK4lEq9gFTK+Hmx88pHqVjuZkFj4SZ2TZgs2JSGjaa2WcA1vsbd28AdgGTFZ9Csx+YaWZn4IKVQDM7DSwIDxDFve8v7E3+RQKEEhwFZgGbFKvC8REwK8wx/ytA70hgZvcQbInSobjlns6w1y++sOf/k+9qZ4ZTxKlAKzCH4OvfxgLDFNdM0k2wc/lRggW+LUBHtW8l+xuWwqBw5I0ApAAAAABJRU5ErkJggg==)](https://raw.githubusercontent.com/chdemko/pandoc-latex-newpage/develop/LICENSE)
[![Python version](https://img.shields.io/pypi/pyversions/pandoc-latex-newpage.svg?logo=Python&logoColor=white)](https://pypi.org/project/pandoc-latex-newpage/)
[![Poetry version](https://img.shields.io/badge/poetry-1.2|1.3|1.4|1.5-blue.svg)](https://python-poetry.org/)
[![Pandoc version](https://img.shields.io/badge/pandoc-2.11|2.12|2.13|2.14|2.15|2.16|2.17|2.18|2.19|3.0|3.1-blue.svg)](https://pandoc.org/)
[![Downloads](https://pepy.tech/badge/pandoc-latex-newpage)](https://pepy.tech/project/pandoc-latex-newpage)
[![Development Status](https://img.shields.io/pypi/status/pandoc-latex-newpage.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIAAAACACAYAAADDPmHLAAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAA3XAAAN1wFCKJt4AAAAB3RJTUUH4gwPFiUnX5lXMAAAAlBJREFUeNrt3b1qlEEUBuB3TNDCP7wDOwv/cgv+pDC3YcDe+xBFFFLoDWhhpxiD12Ch1mJsg7irjRLGYjcKEbLC92n223meMgQSzrx7Zs6wMAkAAAAAAAAAAAAAAAAAAAAw78r+H9RaLyZZT3Itydkkx5XpUH1L8iHJVpJHpZS3/yQAtdZjSe4muZXkiLrPpd0kG0lul1K+9xaA6eK/SHJFjQfhdZIbfYRg75N+z+IPytUkd3rpANM9/422P8jt4HIp5V3XDrBu8QdpKcnNPraA62o5WKt9bAHjJCfUcpDGpZRTXQNQ1fGAApVSDvPvz1qfrv+fvb9xAiAACACDVf80qrU+q7Wecwhs4BB4gM+ZXBRt6wBtOpO/uC7WARa3AyTJqJRyWgdo18xLIgEwBSAACABt3hOYAhZ7Cph9TyAAzQYgSZ4KQNsBGAlA2wFwCDQFIAAIAAKAACAACAACgAAgAAgAAoAAIAAIAIvniwC07aVvBM2wwN8I2kmyogO0Z5TkSZKVUsqnZfVou4PpAKYABAABYDHnfAFofM6feUh0D7Cw9wA7e6OeDtDwnD/rl90DNN6hdABTAAJAs5aTjJOcVIreT+H/68DXuQNsW+bB+thHAF6p42Btdp4iaq0XMnk2bkk9B2U3yaVSyvtOHWD6Fu2Geg7Ow66Ln/x+OvZokueZPBjN/NtKslZK+dHLGDh9g3YtyYNpa2F+2/79vhb/VwfYN/acz+RFytVMno/3puDh+prJ8/GbSR730fYBAAAAAAAAAAAAAAAAAACAYfkJuHbYr8dtGYwAAAAASUVORK5CYII=)](https://pypi.org/project/pandoc-latex-newpage/)
[![Docs](https://img.shields.io/readthedocs/pandoc-latex-newpage.svg?logo=read-the-docs&logoColor=white)](https://pandoc-latex-newpage.readthedocs.io)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAOxAAADsQBlSsOGwAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAANwSURBVGiB7Zndi1VlFIefNZPR9GkTmSkOhIZYeBFiIDEYNUREXVQEQUhK4hdEf0GQf0IUU2BdhHUjNQTpRRdl0NdFXYRZCA0SJTZ9CJEDmY49Xewzw57Xfc7+OGfOEJzn5vCuvfbav/Wutd+993tgwIAB/2ui3xdUVwKPAbcDPwDHIuJiv3XURr1HPaTOuphpdeNy6ytEvUbdoX5pZ75Xr15uvQuoa9WX1N9KhOfZsdyih9QJ9Yg6V0P4PF8sl/CV6gvq6QaiU7b0U/g29bB6oQfC5znUD+HXqu/2UHSeWbNltjJDDXKYBJ4EfgFeBo42iNGO64BnexhvMeoqsxt0Vh3L2V/tYRVOqZUfsHUrcCcwDJyKiJ9y9g9rxunERuDBqs51Ezjb+t2UrwDwcM04Zeyv6lj7XUj9GtgCzABHgA3AI3XjlDAH3BERZ3ocF9TnetjvnThYRU+TCowAZ4DRuufWZAYYi4hLnZxqL6MR8TfwVlNVNVgNPL4kkdUN6uU+tNEnZVo6VkC9tcgeEdPAR83Sr8V29e5ODmUttLvDscn6ehpReUldhLpebTvL6rD6Yx/a6C/1xnY6OlVgf6fjEXEZeKPSbHTHDcAztc5QR9Q/1OOJfSgZr1b/6UMVTrTT2m6GnwZuKbBvVRfW/4iYAaaqT01jNqvjRQfaJdDuxhkBdia21xqKqku1m9ls+2OetIXuN9sGSVvpRB/a6KK6JtVbVIHnS3JcD0wktterTE6XrAB2pcZ0JkfJ+r+MA8n4MHC+sbTq7FGH84a0AjvJ+ryMR819D0TEeeDtruWVMwbcmzcsJGD2GbevYqBhYE9i69eTeVV+kK/ANrJPxqrsNrcdGBEngU+701aJb/ODfAJ1xAPcBjyR2Ja6Cu9FxOm8IZ/AdIOA6c08RfYhshQcB/amxnwCXwHf1Qw6rm6eH7T2+d9sJK+YObJJmYiIByLiXEfv1kPs15IHWcpk4rPOZpu7ec6qB9W1tVNWR9UX1Z8LEhgvuNgVr7vq+w1E/6t+rD6lrqgtvCCRq0x2i9U1rQulHEj8Hqoh/E/1FXVT16IrJjZVIOJk4hPqZyXCv1H3qtf3RXhO3M3qsQJB2xO/dS2ReS6o76j39UpP438p1QlgK3BTy/R5RHyQ+AyRbTveBZwDjkbE702vOWDAgCv5DyyzjR7/CUzHAAAAAElFTkSuQmCC)](https://pypi.org/project/black/)

*pandoc-latex-newpage* is a [pandoc] filter for converting horizontal rule to new page in *LaTeX*.

[pandoc]: http://pandoc.org/

Instructions
------------

*pandoc-latex-newpage* requires [python], a programming language that comes pre-installed on linux and Mac OS X, and which is easily installed [on Windows]

Install *pandoc-latex-newpage* using the bash command

~~~shell
$ pip install pandoc-latex-newpage
~~~

To upgrade to the most recent release, use

~~~shell
$ pip install --upgrade pandoc-latex-newpage
~~~

To upgrade to the current code, use

~~~shell
$ pip install --upgrade --force git+https://github.com/chdemko/pandoc-latex-newpage
~~~

`pip` is a script that downloads and installs modules from the Python Package Index, [PyPI].  It should come installed with your python distribution. If you are running linux, `pip` may be bundled separately. On a Debian-based system (including Ubuntu), you can install it as root using

~~~shell
$ sudo apt-get update
$ sudo apt-get install python3-pip
~~~

[python]: https://www.python.org
[on Windows]: https://www.python.org/downloads/windows
[PyPI]: https://pypi.org


Getting Help
------------

If you have any difficulties with *pandoc-latex-newpage*, please feel welcome to [file an issue] on github so that we can help.

[file an issue]: https://github.com/chdemko/pandoc-latex-newpage/issues

