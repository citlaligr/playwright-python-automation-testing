from playwright.sync_api import Page, expect
#Scenario: Select a radio button
#       Given the user is on the [web page]
#       When the user selects the "Radio1" option
#       Then the radio button should be checked

def test_basic_radiobuttons(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    radio= page.locator("label").filter(has_text="radio1").get_by_role("radio")
    radio.check()
    expect(radio).to_be_checked()
