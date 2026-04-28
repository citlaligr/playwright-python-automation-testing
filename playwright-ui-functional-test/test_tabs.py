from playwright.sync_api import Page, expect

#Scenario: Open a new tab  and validate the body
#       Given the user is on the [web page]
#       When the user clicks on a button
#       Then a new tab should be open with the expected text
def test_opentab(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page).to_have_title("Practice Page")
    expect(page).to_have_url("https://rahulshettyacademy.com/AutomationPractice/")
    with page.expect_popup() as newTab:
        page.locator("#opentab").click()
    tab=newTab.value
    tab.wait_for_load_state()
    expect(tab.locator("body")).to_contain_text("Foundations of Modern Higher Education")
