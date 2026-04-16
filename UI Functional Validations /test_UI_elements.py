from playwright.sync_api import Page, expect, Expect

#Scenario: Select a radio button
#       Given the user is on the [web page]
#       When the user selects the "Radio1" option
#       Then the radio button should be checked

def test_basic_radiobuttons(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    radio= page.locator("label").filter(has_text="radio1").get_by_role("radio")
    radio.check()
    expect(radio).to_be_checked()

#Feature: Autocomplete dropdown selection
#Scenario: Select a country by typing a partial name
#          Given the user is on the [web page]
#          When the user types "can" in the country input
#          And select "Canada" from the suggestions
#          Then the input value should be "Canada"

def test_select_country_by_input(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    placehold=page.get_by_placeholder("Type to Select Countries")
    placehold.type("can")
    optionselected= page.get_by_text("Canada")
    expect(optionselected).to_be_visible()
    optionselected.click()
    expect(placehold).to_have_value("Canada")

#Scenario: Select a country by iterating through dropdown options
#          Given the user is on the [web page]
#          When the user types "can" in the country input
#          And the user iterates through the suggestions
#          And selects the option "Canada"
#          Then the input value should be "Canada"

def test_select_country_from_list(page: Page):
        page.goto("https://rahulshettyacademy.com/AutomationPractice/")

        placehold = page.get_by_placeholder("Type to Select Countries")
        placehold.type("can")

        options = page.locator("ul.ui-menu li div")
        expect(options.first).to_be_visible()
        count = options.count()
        for i in range(count):
            text = options.nth(i).inner_text()
            if text == "Canada":
                options.nth(i).click()
                break
        expect(placehold).to_have_value("Canada")


#Scenario: Validate autocomplete suggestions filtering
#          Given the user is on the practice page
#          When the user types "ca" in the country input
#          Then all the suggested options contains "ca"

def test_dropdown_filters_by_input(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    placehold = page.get_by_placeholder("Type to Select Countries")
    placehold.type("ca")

    options = page.locator("ul.ui-menu li div")
    expect(options.first).to_be_visible()
    count = options.count()
    for i in range(count):
        text = options.nth(i).text_content()
        assert "ca" in text.lower()

#Scenario: Select an option of a dropdown
#       Given the user is on the [web page]
#       When the user selects the Option2 of a dropdown
#       Then the dropdown should appear selected

def test_dropdown(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    dropdown=page.locator("#dropdown-class-example")
    dropdown.select_option("option2")
    expect(page.locator("#dropdown-class-example")).to_have_value("option2")

#Scenario: Check an option of a checkbox
#       Given the user is on the [web page]
#       When the user selects the Option1 of a checkkbox
#       Then the checkbox should appear checked
def test_checkboxes(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    opt_checkbx=page.locator("#checkBoxOption1")
    opt_checkbx.check()
    expect(opt_checkbx).to_be_checked()
