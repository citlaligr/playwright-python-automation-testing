from playwright.sync_api import Page, expect

#Scenario: Validate the successful login
#          Given the user is on the web page
#          When the user type the correct username and password
#          And clicks on Sign In button
#          Then the home page is displayed

def test_succesfulLogin(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.locator("#username").fill("rahulshettyacademy")
    page.locator("#password").fill("Learning@830$3mK2")
    page.get_by_role("button", name="Sign In").click()
    page.wait_for_url("**/shop")
    print(f"url: {page.url}")
    expect(page).to_have_url("https://rahulshettyacademy.com/angularpractice/shop")

#Scenario: Validate the message "Incorrect username/password." adding incorrect data
#          Given the user is on the web page
#          When the user type the wrong username and password
#          And clicks on Sign In button
#          Then it appears the text "Incorrect username/password." without a login successful.

def test_failedLogin(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.locator("#username").fill("wrongUser")
    page.locator("#password").fill("wrongPass")
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()

#Scenario: Validate the message "Empty username/password." leaving empty fields
#          Given the user is on the web page
#          When the user type the wrong username and password
#          And clicks on Sign In button
#          Then it appears the text "Empty username/password." without a login successful.

def test_emptyLogin(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.locator("#username").fill("")
    page.locator("#password").fill("")
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Empty username/password.")).to_be_visible()
