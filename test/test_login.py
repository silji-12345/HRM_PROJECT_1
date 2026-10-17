from playwright.sync_api import Page, sync_playwright, expect

from Pages.ALogin import Logins


def test_Login(url):
    page =url
    credentials = {"user":"Admin", "passw":"admin123"}


    Loginpage = Logins(page)
    Loginpage.Login(credentials["user"], credentials["passw"])









