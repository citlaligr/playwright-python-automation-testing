from playwright.sync_api import Page, expect

#Scenario: Open an external window and validate the body
#       Given the user is on the [web page]
#       When the user clicks on a button
#       Then a new window should be open with the expected text
def test_openwindow(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    with page.expect_popup() as newWindow:
        page.get_by_role("button", name="Open Window").click()
    window=newWindow.value
    expect(window.locator("body")).to_contain_text("Modern higher education")

#Scenario: Validate the correct url
#       Given the user is on the [web page]
#       When the user clicks on a button
#       Then a new window should be open with the correct url

def test_urlwindow(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    with page.expect_popup() as newWindow:
        page.get_by_role("button", name="Open Window").click()
    window=newWindow.value
    expect(window).to_have_url("https://www.dot-consulting.org/articles/foundations-of-modern-higher-education.html?psystem=PW&domain=www.qaclickacademy.com&oref=https%3A%2F%2Fwww.qaclickacademy.com%2F&trafficTarget=reseller")

#Scenario: Validate the correct title
#       Given the user is on the [web page]
#       When the user clicks on a button
#       Then a new window should be open with the correct title

def test_windowTitle(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    with page.expect_popup() as newWindow:
        page.get_by_role("button", name="Open Window").click()
    window=newWindow.value
    expect(window).to_have_title("Foundations of Modern Higher Education | .Consulting")

