import os
from playwright.sync_api import Page

class LTCartPage:
    def __init__(self,page:Page):
        self.page = page
        self.cart_url = f"{os.getenv('LT_URL').strip()}index.php?route=checkout/cart"
        self.checkout_btn = self.page.locator("a.btn-primary").filter(has_text="Checkout")

    def navigate_to_cart(self):
        self.page.goto(self.cart_url)

    def go_to_checkout(self):
        self.checkout_btn.click()