import pytest
from playwright.sync_api import Page

def test_playWrightBasics(playwright):
    # slow_mo=1000 slows each action by 1000ms — great for watching what happens
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()  # store page reference so we can wait/interact
    page.goto("https://www.google.com/")
    page.wait_for_load_state("networkidle")  # wait until network is idle, not just loaded
    page.wait_for_timeout(2000)  # extra 2s so you can see the page
    browser.close()


def test_playWrightShortCut(page: Page):
    # page fixture auto-manages browser lifecycle — no need to call page.close()
    page.goto("https://www.google.com/")
    page.wait_for_load_state("networkidle")
    page.wait_for_timeout(2000)
    # page.pause()  # uncomment this to open Playwright Inspector for step-through debugging

