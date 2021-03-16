"""Test get_ppbrowser."""
import asyncio
import pytest
import pyppeteer
from get_ppbrowser import get_ppbrowser  # , BROWSER, LOOP

#  All test coroutines will be treated as marked.
# pytestmark = pytest.mark.asyncio
# uncomment line7  and change test to async/await

LOOP = asyncio.get_event_loop()


def test_browser():
    """Test BROWSER."""
    BROWSER = LOOP.run_until_complete(get_ppbrowser())
    page = LOOP.run_until_complete(BROWSER.newPage())
    assert isinstance(page, pyppeteer.page.Page)


def test_get_ppbrowser():
    """Test get_ppbrowser."""

    # browser = await get_ppbrowser()
    # page = await browser.newPage()
    browser = LOOP.run_until_complete(get_ppbrowser())
    page = LOOP.run_until_complete(browser.newPage())
    assert isinstance(page, pyppeteer.page.Page)


_ = '''
async def test_ppbrowser_async():
    """test async get_ppbrowser."""
    browser = await get_ppbrowser()
    page = await browser.newPage()
    assert isinstance(page, pyppeteer.page.Page)
# '''
