

from playwright.sync_api import Page, expect

BASE_URL="https://rahulshettyacademy.com/seleniumPractise/"


#Scenario: Validation of empty cart shop
#          Given the user is on the [web page]
#          When the user clicks on the cart shop
#          Then the cart shop is empty with the message: You cart is empty!
#          And there is an image of empty state
#          And the "PROCEED TO CHECKOUT" disabled button

def test_emptyCartShop(page: Page):
    page.goto(BASE_URL)
    page.locator(".cart-icon").click()
    cartshop=page.locator(".cart-preview.active")
    expect(cartshop).to_be_visible()
    #Disabled button
    expect(cartshop.get_by_role("button", name="PROCEED TO CHECKOUT")).to_have_class("disabled")
    #Text
    expect(cartshop.locator(".empty-cart").get_by_text("You cart is empty!")).to_be_visible()
    #Image
    expect(cartshop.locator(".empty-cart").get_by_role("img", name="empty-cart")).to_be_visible()

#Reusable function to get the data of each product
def getProductData(page: Page, product ):

    ProdCard = page.locator(".product").filter(has_text=product)
    # Data product locators
    img=ProdCard.get_by_role("img",name=product)
    prdName=ProdCard.locator(".product-name")
    prdPrice=ProdCard.locator(".product-price")

    return (
        img.get_attribute("src"),
        prdName.text_content(),
        prdPrice.text_content(),
    )

#Reusable function to add a single product
def addProduct(page: Page, product, quantity):
    productCard=page.locator(".product").filter(has_text= product).first

    btn=productCard.get_by_role("button", name="ADD TO CART")
    btn.click()

    expect(btn).to_be_enabled()


#Scenario: Validation of product elements in the cart  after adding it

#          Given the user is on the [web page]
#          When the user add a product
#          And go to the cart shop
#          Then the item added should be displayed with: an image, a name, a price, and the remove icon


def test_CartShopElements(page: Page):
    page.goto(BASE_URL)
    addProduct(page, "Brocolli - 1 Kg")
    page.locator(".cart-icon").click()
    cartshop = page.locator(".cart-preview.active")
    expect(cartshop).to_be_visible()

    # Enabled button
    expect(cartshop.get_by_role("button", name="PROCEED TO CHECKOUT")).to_have_class(" ")
    #Existent stuffs
    item=cartshop.locator(".cart-item")
    productImage=item.locator(".product-image")
    productInfo=item.locator(".product-info")
    productName=item.locator(".product-name")
    productPrice=item.locator(".product-price")
    productTotal=item.locator(".product-total")
    productRemove=item.locator(".product-remove")

    expect(productImage).to_be_visible()
    expect(productInfo).to_be_visible()
    expect(productName).to_be_visible()
    expect(productPrice).to_be_visible()
    expect(productTotal).to_be_visible()
    expect(productRemove).to_be_visible()

#Scenario: Validation of product data in the cart  after adding it

#          Given the user is on the [web page]
#          When the user add a product
#          And go to the cart shop
#          Then the item added should be displayed with: the product image
#          And the product name
#          And the product price
#          And the total per product quantity
#          And the remove icon

def test_cartShopDataProducts(page: Page):
    page.goto(BASE_URL)
    # Getting data product from the catalog
    image, pName, pPrice = getProductData(page,"Brocolli - 1 Kg")

    brocoliCard = page.locator(".product").filter(has_text="Brocolli - 1 Kg")
    brocoliCard.locator(".increment").click()
    brocoliCard.locator(".increment").click()
    pQuantity = brocoliCard.locator(".quantity").get_attribute("value")

    # Adding product to the cart
    brocoliCard.get_by_role("button", name="ADD TO CART").click()

    #Get data product from the cart
    page.locator(".cart-icon").click()
    cartshop = page.locator(".cart-preview.active")
    expect(cartshop).to_be_visible()
    item = cartshop.locator(".cart-item")

    totalperProd= str(int(pPrice) *int(pQuantity))

    #Compare data catalog vs cartshop

    expect(item.locator(".product-image")).to_have_attribute("src", image)
    expect(item.locator(".product-info").locator(".product-name")).to_have_text(pName)
    expect(item.locator(".product-info").locator(".product-price")).to_have_text(pPrice)
    expect(item.locator(".product-total").locator(".quantity")).to_contain_text(pQuantity)
    expect(item.locator(".product-total").locator(".amount")).to_have_text(totalperProd)


#Scenario: Verify product removal from cart
#          Given the user is on the [web page]
#          When the user add a product
#          And go to the cart shop
#          And click on the remove icon
#          Then the product should be removed
#
#Note: For this test the scenario was designed to add a single element and removed it, leaving the empty state



def test_removeProduct(page: Page):
    page.goto(BASE_URL)
    addProduct(page, "Brocolli - 1 Kg")
    page.locator(".cart-icon").click()
    cartshop = page.locator(".cart-preview.active")
    expect(cartshop).to_be_visible()
    item = cartshop.locator(".cart-item")
    productRemove = item.locator(".product-remove")
    productRemove.click()
    expect(cartshop.get_by_role("button", name="PROCEED TO CHECKOUT")).to_have_class("disabled")
    #Text
    expect(cartshop.locator(".empty-cart").get_by_text("You cart is empty!")).to_be_visible()
    #Image
    expect(cartshop.locator(".empty-cart").get_by_role("img", name="empty-cart")).to_be_visible()

#Scenario: Verify the adding of 4 items with different quantities to the cart with their expected values
#         Given the user is on the [web page]
#         When the user add 4 different products selecting different quantities
#         Then each product is added to the cart
#         And their details are displayed as it is expected
#         And the total of each product is displayed as it is expected



def test_multipleProductsaddedCart(page: Page):

    page.goto(BASE_URL)
    # Getting data product from the catalog
    imageBroc, pNameBroc, pPriceBroc = getProductData(page, "Brocolli - 1 Kg")
    imageMush, pNameMush, pPriceMush = getProductData(page, "Mushroom - 1 Kg")
    imagePump, pNamePump, pPricePump = getProductData(page, "Pumpkin - 1 Kg")
    imageCorn, pNameCorn, pPriceCorn = getProductData(page, "Corn - 1 Kg" )

    #Adding Products
    addProduct(page, "Brocolli - 1 Kg", 5)
    addProduct(page, "Mushroom - 1 Kg", 1)
    addProduct(page, "Pumpkin - 1 Kg", 5)
    addProduct(page, "Corn - 1 Kg", 7)

    cart = openCart(page)

    cartShopData(page, cart, imageBroc, pNameBroc, pPriceBroc)
    cartShopData(page, cart, imageMush, pNameMush, pPriceMush)
    cartShopData(page, cart, imagePump, pNamePump, pPricePump)
    cartShopData(page, cart, imageCorn, pNameCorn, pPriceCorn)

#Reusable function to open the cart element
def openCart(page:Page):
    cartshop = page.locator(".cart-preview.active")
    if not cartshop.is_visible():
        page.locator(".cart-icon").click()
    expect(cartshop).to_be_visible()
    return cartshop
#Reusable function to validate the details of each product in the catalog versus the ones displayed in the cart
def cartShopData(page:Page, cart, image,pName,pPrice):

    item = cart.locator(".cart-item")
    expect(item).to_have_count(4)
    singleitem=item.filter(has_text=pName)

    quantityPrevSelected=quantitySelected(page,pName)
    totalperProd = str(int(pPrice) * int(quantityPrevSelected))

    # Compare data catalog vs cartshop

    expect(singleitem.locator(".product-image")).to_have_attribute("src", image)
    expect(singleitem.locator(".product-info").locator(".product-name")).to_have_text(pName)
    expect(singleitem.locator(".product-info").locator(".product-price")).to_have_text(pPrice)
    expect(singleitem.locator(".product-total").locator(".quantity")).to_contain_text(quantityPrevSelected)
    expect(singleitem.locator(".product-total").locator(".amount")).to_have_text(totalperProd)

#Reusable function to increment the quantity of each product
def quantityCalculate(page:Page, pName,quant):

    prodCard = page.locator(".product").filter(has_text=pName).first
    print(prodCard.text_content())
    increment=prodCard.locator(".increment")
    print(f"quantity:{quant}")
    if quant > 1:
        for i in range(quant-1):
            increment.click()

#Reusable function to get the value of the quantity selected
def quantitySelected(page:Page, pName):
    prodCard = page.locator(".product").filter(has_text=pName).first
    pQuantity = prodCard.locator(".quantity").get_attribute("value")
    strQuantity=str(pQuantity)
    return strQuantity


