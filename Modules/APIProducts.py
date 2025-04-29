import json
import requests

class ApiProducts:
    # Different API method calls for CRUD operations for Product category
    def addNewProduct(self,Url,header,data):
        response =requests.post(url=Url,json=data,headers=header)
        return response

    def getDataForAllProducts(self,baseUrl,header,limit,skip):
        baseUrl= baseUrl + f"?$limit={limit}&$skip={skip}"
        response = requests.get(baseUrl, headers=header)
        return response

    def getDataForSpecificProduct(self,baseUrl,Header,productId):
        baseUrl=baseUrl + str(productId)
        print(baseUrl)
        response=requests.get(baseUrl,headers=Header)
        return response

    def UpdateProduct(self,baseUrl,Data,Header,productId):
        baseUrl= baseUrl+ str(productId)
        response =requests.patch(url=baseUrl,json=Data,headers=Header)
        return response


    def deleteProduct(self,baseUrl,header,productId):
        baseUrl= baseUrl + str(productId)
        response = requests.delete(baseUrl,headers=header)
        return response

