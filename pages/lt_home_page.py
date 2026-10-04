import os
from dotenv import load_dotenv

load_dotenv()

class LTHomePage:
    def __init__(self,page):
        self.page = page
        self.url = os.getenv("LT_URL").strip()
        self.search_input = self.page.locator("input[name='search']").first
        self.search_button = self.page.locator("button:has-text('Search')").first

    def navigate(self):
        self.page.goto(self.url)

    def search_for_product(self,product_name):
        self.search_input.fill(product_name)
        self.search_button.click()