from playwright.sync_api import Page, expect


#Scenario: To get the total of rows and columns 

def test_rowsAndColumnTotal(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    legend = page.get_by_text("Web Table Example")
    curses = legend.locator("..").locator("table")
    total_columns = curses.locator("th").count()
    assert total_columns==3
    total_rows = curses.locator("tr").count()
    assert  total_rows==11


#Scenario: To get the price of a specific curse 

def test_rowsAndColumnTotal(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    legend = page.get_by_text("Web Table Example")
    curses = legend.locator("..").locator("table")
    for i in range(curses.locator("th").count()):
        if curses.locator("th").nth(i).filter(has_text="Price").count()>0:
            PriceCol=i
            print(f"Price column is: {PriceCol}")
            break
    curseRow=curses.locator("tr").filter(has_text="Learn SQL in Practical + Database Testing from Scratch")
    expect(curseRow.locator("td").nth(PriceCol)).to_have_text("25")




