import os
from faker import Faker

class LTRegisterPage:
    def __init__(self,page):
        self.page = page
        self.fake = Faker()
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

    def fill_registration_form(self):
        fake_password = self.fake.password(length=10)

        self.first_name.fill(self.fake.first_name())
        self.last_name.fill(self.fake.last_name())
        self.email.fill(self.fake.email())

        fake_phone = ''.join(filter(str.isdigit, self.fake.phone_number()))[:10]
        self.telephone.fill(fake_phone)

        self.password.fill(fake_password)
        self.confirm_password.fill(fake_password)

        self.agree_checkbox.click()
        self.continue_btn.click()