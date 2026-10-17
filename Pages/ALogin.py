from Pages.BAdmin import Admin
class Logins:

    def __init__(self,Page):
        self.page = Page
        self.username = self.page.get_by_placeholder("Username")
        self.password = self.page.get_by_placeholder("Password")
        self.login_click = self.page.locator("//button[normalize-space()='Login']")


    def Login(self,user,passw):
        self.username.fill(user)
        self.password.fill(passw)
        self.login_click.click()

        return Admin(self.page)






