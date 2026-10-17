from playwright.sync_api import Page, sync_playwright, expect

from Pages.ALogin import Logins
from Pages.BAdmin import Admin


def test_Admin(url):
    page =url
    credentials = {
        "user": "Admin",
        "passw": "admin123",
        "name": "Ayush21"
    }

    Loginpage = Logins(page)
    Loginpage.Login(credentials["user"], credentials["passw"])


    admin = Admin(page)
    admin.admin_page(credentials["name"])












