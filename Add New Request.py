# import json
# import requests
#
#
# def addNewProduct():
#     baseUrl="http://localhost:3030/products"
#     header = {
#         "Accept": "application/json",
#         "Content-type": "application/json"
#     }
#
#     data = {
#             "name": "Necklace set",
#             "type": "Jewellery",
#             "price": 280,
#             "shipping": 20,
#             "upc": "021333422019",
#             "description": "Diamond Platinum necklace",
#             "manufacturer": "KJewelers",
#             "model": "NC1400DPZ",
#             "url": "http://www.bestbuy.com/",
#             "image": "http://img.bbystatic.com/BestBuy_US/images/products/1111/1111_sa.jpg"
#     }
#     response =requests.post(url=baseUrl,json=data,headers=header)
#     if response.status_code==400:
#         print("Error occurred while displayed the specific product data")
#     # Validating proper response code as 201 for successful operation
#     assert response.status_code == 201
#     json_data= response.json()
#     assert json_data["name"]=="Necklace set"
#     productId=json_data["id"]
#     print(productId)
#     print("New Product has been added successfully")
#     json_data = json.dumps(json_data,indent=4)
#     print(json_data)
#
#     return productId
#
# def getDataForAllProducts(limit,skip):
#     baseUrl=f"http://localhost:3030/products?$limit={limit}&$skip={skip}"
#     print(baseUrl)
#     header={
#                 "Accept": "application/json"
#             }
#     response = requests.get(baseUrl, headers=header)
#     #Validating proper response code as 200 for successful operation
#     assert response.status_code == 200
#     # Validating proper response header content type
#     assert response.headers['content-type'] == "application/json; charset=utf-8"
#     json_data = response.json()
#     #validating whether limit displayed is as per input variable
#     assert json_data["limit"]==limit
#     # validating whether skip displayed is as per input variable
#     assert json_data["skip"]==skip
#     #printing some additional information about products
#     print("Total products in database are :",json_data['total'])
#     print(f"Displayed only {limit} after skipping {skip} products")
#     #displaying json data in some presentable format
#     json_data = json.dumps(json_data, indent=4)
#     print(json_data)
#
# def getDataForSpecificProduct(productId):
#     baseUrl="http://localhost:3030/products/" + str(productId)
#     print(baseUrl)
#     header = {
#                  "Accept": "application/json"
#              }
#     response=requests.get(baseUrl,headers=header)
#
#     if response.status_code==400:
#         print("Error occurred while displayed the specific product data")
#     # Validating proper response code as 200 for successful operation
#     assert response.status_code == 200
#     # Validating proper response header content type
#     assert response.headers['content-type'] == "application/json; charset=utf-8"
#
#     json_data=response.json()
#     #validating whether data displayed is for the passed Product
#     assert json_data["id"]==productId
#     # displaying json data in some presentable format
#     json_data=json.dumps(json_data,indent=4)
#     print(json_data)
#
# def UpdateProduct(productId):
#     baseUrl="http://localhost:3030/products/" + str(productId)
#     header = {
#         "Accept": "application/json",
#         "Content-type": "application/json"
#     }
#
#     data = {
#         "id": productId,
#         "name": "Necklace set No " + str(productId),
#         "type": "Jewellery",
#         "price": 280,
#         "upc": "021333422019",
#         "shipping": 10,
#         "description": "Diamond Platinum necklace",
#         "manufacturer": "KJewelers and KC",
#         "model": "NC1400DPZ",
#         "url": "http://www.bestbuy.com/",
#         "image": "http://img.bbystatic.com/BestBuy_US/images/products/1111/1111_sa.jpg",
#
#     }
#     print(data)
#     response =requests.patch(url=baseUrl,json=data,headers=header)
#     if response.status_code == 400:
#         print("Unexpected error happened. Not able to update the product data")
#     elif response.status_code==404:
#         print("Unable to locate the product in database to delete")
#     print(response.status_code)
#
#     # Validating proper response code as 200 for successful operation
#     assert response.status_code == 200
#     json_data= response.json()
#     # validating whether data displayed is for the passed Product
#     assert json_data["id"] == productId
#     assert json_data["manufacturer"]=="KJewelers and KC"
#     assert json_data["shipping"] == 10
#     json_data = json.dumps(json_data,indent=4)
#     print("Data updated successfully. Update data is like this :")
#     print(json_data)
#
#
# def deleteProduct(requestId):
#     baseUrl="http://localhost:3030/products/"+ str(requestId)
#     header={"Accept": "application/json"}
#     response = requests.delete(baseUrl,headers=header)
#     if response.status_code==400:
#         print("Unexpected error happened. Not able to delete")
#     elif response.status_code==404:
#         print("Unable to locate the product in database to delete")
#     # Validating proper response code as 200 for successful operation
#     assert response.status_code == 200
#     print("Product Deleted Successfully")
#     # if "Product deleted" in response.text:
#     #     print("Product Deleted Successfully")
#
#
# getDataForAllProducts(2,0)
#
# productID= addNewProduct()
# getDataForSpecificProduct(productID)
# UpdateProduct(productID)
# deleteProduct(productID)

