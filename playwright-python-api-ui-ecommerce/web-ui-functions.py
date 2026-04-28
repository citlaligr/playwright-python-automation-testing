import os

from playwright.sync_api import Page
from cit_practice.cit_practice_api.API_methods import API_methods

EMAIL = os.getenv("email@gmail.com")
PASSWORD= os.getenv("password")



def test_web_ui(page:Page, playwright):
    api_meth=API_methods()
    token=api_meth.get_token(playwright)
    orderID, productID=api_meth.create_order(playwright,token)
    name, productImage, productPrice=api_meth.get_product_details(playwright,token, productID)
    productNameOrdered, productImageOrdered, productPriceOrdered= api_meth.get_order_details(playwright,token, orderID)

    page.goto("https://rahulshettyacademy.com/client")#SERVER

    #LOGIN
    page.get_by_placeholder("email@example.com").fill(EMAIL) #FE
    page.get_by_placeholder("enter your passsword").fill(PASSWORD)  #FE
    page.get_by_role("button", name="Login").click()  #FE
    page.get_by_role("button", name="ORDERS").click()  #FE


    assert name == productNameOrdered
    assert productImage == productImageOrdered
    assert int(productPrice) == int(productPriceOrdered





