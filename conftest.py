import json

import pytest
import os

@pytest.fixture(scope="class")
def oneTimeSetup():

    print("Method Setup")
    yield
    print("Method teardown")

@pytest.fixture()
def loadTestData():
    #
    fileName ="testData\\testData.json"
    absFileDir= os.path.dirname(__file__)
    ParentPath=os.path.dirname(absFileDir)
    fileName = os.path.join(absFileDir, "testData", "testData.json")
    print(fileName)
    with open(fileName) as json_file:
        data = json.load(json_file)
    return data