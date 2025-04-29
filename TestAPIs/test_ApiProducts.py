from Modules.APIProducts import ApiProducts
import pytest
import json


# fixture created to manage and share the API chaining across different Test methods
@pytest.fixture(scope="class")
def my_fixture():
    return {}

@pytest.mark.usefixtures("oneTimeSetup")
class TestApiProducts():


    # Class specific implementation such as creation of ModuleObject Class
    @pytest.fixture(autouse=True)
    def classSetUp(self):
        self.ap = ApiProducts()


    def test_getAllProducts(self,loadTestData):
        #Accessing data from testdata file
        data = loadTestData["GetAll"]
        self.getApiUrl = data["getApiUrl"]
        self.getHeader = data["getHeader"]
        self.limit = data["limit"]
        self.skip = data["skip"]

        self.response = self.ap.getDataForAllProducts(self.getApiUrl, self.getHeader, self.limit, self.skip)
        # Validating proper response code as 200 for successful operation
        assert self.response.status_code == 200
        # Validating proper response header content type
        assert self.response.headers['content-type'] == "application/json; charset=utf-8"
        json_data = self.response.json()
        # validating whether limit displayed is as per input variable
        assert json_data["limit"] == self.limit
        # validating whether skip displayed is as per input variable
        assert json_data["skip"] == self.skip
        # printing some additional information about products
        print("Total products in database are :", json_data['total'])
        print(f"Displayed only {self.limit} after skipping {self.skip} products")
        print("**********************************************************************************************")
        # displaying json data in some presentable format
        json_data = json.dumps(json_data, indent=4)
        print(json_data)



    #This test method will test the creation of new Product and assertion for status code as 201
    def test_AddProduct(self,my_fixture,loadTestData):
        data = loadTestData["Post"]
        self.apiUri = data["apiUri"]
        self.PostHeader = data["PostHeader"]
        self.PostPayload=data["PostPayload"]

        self.response = self.ap.addNewProduct(self.apiUri,self.PostHeader,self.PostPayload)
        if self.response.status_code == 400:
            print("Error occurred while displayed the specific product data")
            # Validating proper response code as 201 for successful operation
        assert self.response.status_code == 201
        json_data = self.response.json()
        assert json_data["name"] == "Necklace set"
        my_fixture["id"]=json_data["id"]
        print(f"New Product {json_data["id"]} has been added successfully")
        json_data = json.dumps(json_data, indent=4)
        print(json_data)
        print("*************************************************************************************************")

    # This test method will test the retrieval of details for Specific Product(Here we are testing it for newly created product
    # and assertions for status code as 200,correct content type and correct id of Product
    def test_getSpecificProduct(self,my_fixture,loadTestData):
        data = loadTestData["SpecificProduct"]
        self.getSPbaseUrl = data["getSPbaseUrl"]
        self.getSPHeader = data["getSPHeader"]
        self.spProductId = my_fixture["id"]
        self.response=self.ap.getDataForSpecificProduct(self.getSPbaseUrl,self.getSPHeader,self.spProductId)

        if self.response.status_code==400:
            print("Error occurred while displayed the specific product data")
        # Validating proper response code as 200 for successful operation
        assert self.response.status_code == 200
        # Validating proper response header content type
        assert self.response.headers['content-type'] == "application/json; charset=utf-8"

        json_data=self.response.json()
        #validating whether data displayed is for the passed Product
        assert json_data["id"]==self.spProductId
        # displaying json data in some presentable format
        json_data=json.dumps(json_data,indent=4)
        print(f"The data for product {self.spProductId} is :")
        print(json_data)
        print("**********************************************************************************")

    # This test method will test the Update of details for Specific Product(Here we are testing it for newly created product
    # and assertions for status code as 200,correct updated details
    def test_UpdateProduct(self,my_fixture,loadTestData):
        data = loadTestData["UpdateProduct"]
        self.patchBaseUrl = data["patchBaseUrl"]
        self.patchheader = data["patchheader"]
        self.patchData = data["patchData"]
        self.spProductId = my_fixture["id"]
        self.response = self.ap.UpdateProduct(self.patchBaseUrl,self.patchData,self.patchheader,self.spProductId)
        if self.response.status_code == 400:
            print("Unexpected error happened. Not able to update the product data")
        elif self.response.status_code==404:
            print("Unable to locate the product in database to delete")
        print(self.response.status_code)

        # Validating proper response code as 200 for successful operation
        assert self.response.status_code == 200
        json_data= self.response.json()
        # validating whether data displayed is for the passed Product
        assert json_data["id"] == self.spProductId
        assert json_data["manufacturer"]=="KJewelers and KC"
        assert json_data["shipping"] == 10
        json_data = json.dumps(json_data,indent=4)
        print("Data updated successfully. Update data is like this :")
        print(json_data)
        print("**************************************************************************************")
    #
    # This test method will test the deletion of  Specific Product(Here we are testing it for newly created product
    # and assertions for status code as 200
    def test_deleteProduct(self,my_fixture,loadTestData):
        data = loadTestData["DeleteProduct"]
        self.deleteBaseUrl = data["deleteBaseUrl"]
        self.deleteHeader = data["deleteHeader"]
        self.spProductId=my_fixture["id"]
        self.response = self.ap.deleteProduct(self.deleteBaseUrl,self.deleteHeader,self.spProductId)
        if self.response.status_code==400:
            print("Unexpected error happened. Not able to delete")
        elif self.response.status_code==404:
            print("Unable to locate the product in database to delete")
        # Validating proper response code as 200 for successful operation
        assert self.response.status_code == 200
        print("Product Deleted Successfully")
