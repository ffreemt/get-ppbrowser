# get-ppbrowser
[![build-and-pytest](https://github.com/ffreemt/get-ppbrowser/actions/workflows/build-and-pytest.yml/badge.svg)](https://github.com/ffreemt/get-ppbrowser/actions/workflows/build-and-pytest.yml)[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)[![PyPI version](https://badge.fury.io/py/get-ppbrowser.svg)](https://badge.fury.io/py/get-ppbrowser)

Instantiate a pyppeteer browser object.

## Instalation
```bash
pip install get-ppbrowser
# pip  install get-ppbrowser -U  # to upgrade
```
or
```bash
poetry add get-ppbrowser
# poetry add get-ppbrowser@latest  # to upgrade
```

## Usage
```python
from get_ppbrowser import get_ppbrowser

browser = await get_ppbrowser()
page = waitbrowser.newPage()
await page.goto("http://www.example.com")
```

### PPBROWSER_HEADFUL, PPBROWSER_DEBUG, PPBROWSER_PROXY
Environment variables can be set with, for example, in Windows

```bash
set PPBROWSER_HEADFUL=1
```

or in Linux/iOS
```bash
export PPBROWSER_HEADFUL=1
```
or in `python`

```python
import os

os.environ["PPBROWSER_HEADFUL"] = "1"
```
