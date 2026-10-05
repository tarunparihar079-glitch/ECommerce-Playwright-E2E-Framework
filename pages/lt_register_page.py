import os

class LTRegisterPage:
    def __init__(self,page):
        self.page = page
        self.url = f"{os.getenv('LT_URL').strip()}index.php?route=account/register"

        self.first_name = self.page.get_by_placeholder("First Name")
        self.last_name = self.page.get_by_placeholder("Last Name")
        self.email = self.page.get_by_placeholder("E-Mail")
        self.telephone = self.page.get_by_placeholder("Telephone")
        self.password = self.page.locator("#input-password")
        self.confirm_password = self.page.locator("#input-confirm")

        self.agree_checkbox = self.page.locator("label").filter(has_text="Privacy Policy")
        self.continue_btn = self.page.locator("input[value='Continue']")

    def navigate(self):
        self.page.goto(self.url)

    def fill_registration_form(self, fname, lname, email, phone, password):
        self.first_name.fill(fname)
        self.last_name.fill(lname)
        self.email.fill(email)
        self.telephone.fill(phone)
        
        self.password.fill(password)
        self.confirm_password.fill(password)

        self.agree_checkbox.click()
        self.continue_btn.click()