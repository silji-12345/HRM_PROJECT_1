import pytest

from playwright.sync_api import Page

@pytest.fixture()
def url(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    yield page
