from playwright.sync_api import Page,expect
from pages.lt_home_page import LTHomePage
from pages.lt_search_page import LTSearchPage
from pages.lt_register_page import LTRegisterPage

def test_e2e_register_and_add_to_cart(page:Page):
    register_page = LTRegisterPage(page)
    home_page = LTHomePage(page)
    search_page = LTSearchPage(page)

    register_page.navigate()
    register_page.fill_registration_form()

    expect(page).to_have_title("Your Account Has Been Created!")

    search_keyword = "iMac"
    target_product = "iMac"

    home_page.navigate()
    home_page.search_for_product(search_keyword)
    expect(page).to_have_title("Search - iMac")

    search_page.select_product(target_product)
    expect(page.locator("h1")).to_have_text(target_product)

    page.get_by_role("button",name="Add to Cart").first.click()

    expect(page.locator(".toast-body").first).to_contain_text("Success: You have added")