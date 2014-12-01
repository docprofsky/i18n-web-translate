i18n-web-translate
==================
This is a tool for translating i18n files in a JSON format automatically using
Google Translate.

To run this run `python i18n-translate.py path/to/file target-language input-language`
The target language to translate to is the language tag (Spanish is es).
The input language is the language that the input file is in.

# Pre-requisites
## Python 2
This is written for [Python](https://www.python.org/) 2.7. Any Python 2 version
should work. Python is needed to run this script.

## goslate
This uses [goslate](https://pypi.python.org/pypi/goslate) to interface with
Google Translate. To install it run `pip install goslate`
