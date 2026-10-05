from playwright.sync_api import Page

class LTCheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.firstname_input = self.page.locator("#input-payment-firstname")
        self.lastname_input = self.page.locator("#input-payment-lastname")
        self.address_input = self.page.locator("#input-payment-address-1")
        self.city_input = self.page.locator("#input-payment-city")
        self.postcode_input = self.page.locator("#input-payment-postcode")
        self.country_dropdown = self.page.locator("#input-payment-country")
        self.region_dropdown = self.page.locator("#input-payment-zone")
        self.terms_checkbox = self.page.locator("label[for='input-agree']")
        self.continue_btn = self.page.locator("#button-save")

    def fill_billing_details(self, fname, lname, address, city, postcode):
        self.firstname_input.fill(fname)
        self.lastname_input.fill(lname)
        self.address_input.fill(address)
        self.city_input.fill(city)
        self.postcode_input.fill(postcode)

    def select_country_and_state(self, cname, sname):
        self.country_dropdown.select_option(label=cname)
        self.page.wait_for_timeout(1000)
        self.region_dropdown.select_option(label=sname)

    def agree_and_checkout(self):
        self.page.wait_for_timeout(3000)
        self.terms_checkbox.click(force=True)
        self.page.wait_for_timeout(1000)
        self.continue_btn.click(force=True)
        self.page.wait_for_timeout(2000)
        
        if self.page.locator("#button-confirm").is_visible():
            self.page.locator("#button-confirm").click(force=True)