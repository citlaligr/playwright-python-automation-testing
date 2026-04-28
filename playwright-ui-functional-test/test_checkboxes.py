from playwright.sync_api import Page, expect

#Scenario: Check an option of a checkbox
#       Given the user is on the [web page]
#       When the user selects the Option1 of a checkkbox
#       Then the checkbox should appear checked
def test_checkboxes(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    opt_checkbx=page.locator("#checkBoxOption1")
    opt_checkbx.check()
    expect(opt_checkbx).to_be_checked()
