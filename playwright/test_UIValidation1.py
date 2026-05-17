import pytest 
from playwright.sync_api import Page,expect

def test_UIValidationDynamicScript(playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=800)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username").fill("rahulshettyacademy")
    page.get_by_label("Password").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link",name="terms and conditions").click()
    page.get_by_role("button",name="Sign In").click()
    
    # get the app-card name and assert it with the expected name
    iPhoneProduct = page.locator("app-card").filter(has_text="iPhone X")
    iPhoneProduct.get_by_role("button").click()
    page.wait_for_timeout(2000)
    nokiaEdge = page.locator("app-card").filter(has_text="Nokia Edge")
    nokiaEdge.get_by_role("button").click()
    page.wait_for_timeout(2000)
    
    # Now click on the checkout button and assert the total price
    page.get_by_text("Checkout").click()
  
    
    # Now use the assertion to validate the total number of items 
    expect(page.locator(".media-body")).to_have_count(2)
    

    
    