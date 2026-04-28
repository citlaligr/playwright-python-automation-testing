from playwright.sync_api import Page, expect

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
