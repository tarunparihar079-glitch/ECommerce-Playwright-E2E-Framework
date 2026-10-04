class LTSearchPage:
    def __init__(self,page):
        self.page = page

    def select_product(self,exact_product_name):
        self.page.get_by_text(exact_product_name,exact=True).first.click()