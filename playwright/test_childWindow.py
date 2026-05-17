def test_childWindow(playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=800)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    with page.expect_popup() as newPageInfo:
        page.locator(".blinkingText").click()
        childPage = newPageInfo.value # This will retrive the child page object 
        text = childPage.locator(".red").text_content
        print(text)
