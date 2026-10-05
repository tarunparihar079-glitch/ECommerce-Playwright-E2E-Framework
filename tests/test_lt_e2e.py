import pytest
from faker import Faker
from playwright.sync_api import Page,expect
from utils.api_helpers import get_real_user_from_api
from pages.lt_home_page import LTHomePage
from pages.lt_search_page import LTSearchPage
from pages.lt_register_page import LTRegisterPage
from pages.lt_cart_page import LTCartPage
from pages.lt_checkout_page import LTCheckoutPage

fake = Faker()

@pytest.mark.parametrize("search_keyword,target_product",[
    ("iMac","iMac"),
    ("HTC","HTC Touch HD")
    ])

def test_e2e_register_and_add_to_cart(page:Page,search_keyword,target_product):
    api_fname, api_lname, api_email = get_real_user_from_api()
    register_page = LTRegisterPage(page)
    home_page = LTHomePage(page)
    search_page = LTSearchPage(page)
    cart_page = LTCartPage(page)
    checkout_page = LTCheckoutPage(page)

    register_page.navigate()
    
    fake_password = fake.password(length=10)
    fake_phone = ''.join(filter(str.isdigit,fake.phone_number()))[:10]
    
    register_page.fill_registration_form(
        fname=api_fname, 
        lname=api_lname, 
        email=api_email, 
        phone=fake_phone, 
        password=fake_password
    )
    
    expect(page).to_have_title("Your Account Has Been Created!")

    home_page.navigate()
    home_page.search_for_product(search_keyword)
    expect(page).to_have_title(f"Search - {search_keyword}")

    search_page.select_product(target_product)
    expect(page.locator("h1")).to_have_text(target_product)

    page.get_by_role("button",name="Add to Cart").first.click()
    expect(page.locator(".toast-body").first).to_contain_text("Success: You have added")

    cart_page.navigate_to_cart()
    expect(page).to_have_title("Shopping Cart")
    cart_page.go_to_checkout()

    expect(page).to_have_title("Checkout")
    checkout_page.fill_billing_details(
        fname=api_fname,
        lname=api_lname,
        address=fake.street_address(),
        city=fake.city(),
        postcode=fake.postalcode()
    )

    checkout_page.select_country_and_state("India","Rajasthan")
    checkout_page.agree_and_checkout()