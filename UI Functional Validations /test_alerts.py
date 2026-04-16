from playwright.sync_api import Page, expect

#Scenario: Validate the warning message and the Accept button
#       Given the user is on the [web page]
#       When the user type a name
#       And the user clicks on a button
#       Then a warning message  should be open with the name previously open

def test_warningOK(page: Page):
    name="Citlali"
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.locator("#name").fill(name)

    def handle_message(dialog):
        assert name in dialog.message
        dialog.accept()

    page.on("dialog",handle_message)
    page.locator("#confirmbtn").click()

#Scenario: Validate the Cancel button in the warning message
#       Given the user is on the [web page]
#       When the user type a name
#       And the user clicks on a button
#       Then a warning message should be open with the name previously open
#       When the user clicks on Cancel button
#       Then warning message is closed

def test_warningNOK(page: Page):
    name="Citlali"
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.locator("#name").fill(name)

    def handle_message(dialog):
        assert name in dialog.message
        dialog.dismiss()
    page.on("dialog",handle_message)
    page.locator("#confirmbtn").click()
