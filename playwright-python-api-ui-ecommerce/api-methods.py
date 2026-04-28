from playwright.sync_api import Playwright

payload_create_order = {"orders": [{"country": "Algeria", "productOrderedId": "6960eac0c941646b7a8b3e68"}]}
payload_login = {"userEmail": "gr.citlaligarcia@gmail.com", "userPassword": "Cholula2026!"}

class API_methods:
    # CALL LOGIN API TO GET TOKEN

    def get_token(self, playwright: Playwright):
        api_request_login = playwright.request.new_context(base_url="https://rahulshettyacademy.com/client")
        response = api_request_login.post("/api/ecom/auth/login", data=payload_login)
        assert response.status == 200
        json = response.json()
        token = json["token"]

        return token

    # CALLING CREATE ORDER API TO GET ORDER_ID
    def create_order(self,playwright: Playwright,token):
        # CALLING SERVER
        api_request = playwright.request.new_context(base_url="https://rahulshettyacademy.com/client")
        response = api_request.post("/api/ecom/order/create-order", data=payload_create_order,
                                    headers={"Authorization": token, "Content-Type":"application/json"})
        assert response.status == 201
        body_order_created = response.json()
        orderID = body_order_created["orders"][0]
        productID=body_order_created["productOrderId"][0]
        return orderID, productID


    def get_product_details(self, playwright:Playwright, token, productID):
        #CALLING SERVER
        api_request=playwright.request.new_context(base_url="https://rahulshettyacademy.com/client")
        request_product_details=api_request.get(f"/api/ecom/product/get-product-detail/{productID}",headers={"Authorization": token})
        assert request_product_details.status == 200
        body_product_detailed=request_product_details.json()
        name= body_product_detailed["data"]["productName"]
        productImage = body_product_detailed["data"]["productImage"]
        productPrice = body_product_detailed["data"]["productPrice"]

        return name, productImage, productPrice


    def get_order_details(self, playwright:Playwright,token, orderid):
        api_request = playwright.request.new_context(base_url="https://rahulshettyacademy.com/client")
        order_details=api_request.get(f"/api/ecom/order/get-orders-details?id={orderid}", headers={"Authorization":token})
        assert order_details.status == 200
        body_order_details=order_details.json()

        productNameOrdered=body_order_details["data"]["productName"]
        productImageOrdered=body_order_details["data"]["productImage"]
        productPriceOrdered=body_order_details["data"]["orderPrice"]

        return productNameOrdered, productImageOrdered, productPriceOrdered
