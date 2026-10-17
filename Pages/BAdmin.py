
class Admin:

    def __init__(self,page):

        self.page =page
        self.admin_button = self.page.locator("//span[text()='Admin']")
        self.user_textbox= self.page.locator("//label[text()='Username']/following::input[1]")
        self.search_click = self.page.locator("//button[normalize-space()='Search']")

    def admin_page(self,name):
        self.admin_button.click()
        self.user_textbox.fill(name)
        self.search_click.click()



