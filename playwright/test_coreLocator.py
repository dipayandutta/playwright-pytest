import pytest 
from playwright.sync_api import Page 

def test_coreLocator(playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=800)
    context = browser.new_context()
    page = context.new_page()
    page.goto("file:///Users/dipayandutta/Developer/python/testing/playwright/login.html")
    page.get_by_label("Username").fill("admin")
    page.get_by_label("Password").fill("admin")
    page.get_by_role("combobox").select_option("admin")
    page.locator("#terms").check()
    page.get_by_role("button", name="Login").click()
    page.wait_for_timeout(2000)
    browser.close()

    