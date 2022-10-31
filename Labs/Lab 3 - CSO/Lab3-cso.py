import requests
import json

# After analising the url we can see that "FIQ02" is tge name of the database. So we can slice the url in two parts
# making it easier to change the database so we can reuse this code to call diferent databses 

urlStart = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
urlEnd= "/JSON-stat/1.0/en"



# Saving the information on a file called cso.json as write text
def getAllFile(dataset):
    with open("cso.json", "wt") as fp:
        print(json.dumps(getAll(dataset)), file=fp)

# Function to get all data from the url
def getAll(dataset):
    #Using get to retrieve the information to the URL and converting it to json
    url = urlStart + dataset + urlEnd
    response = requests.get(url)
    return response.json()


def formatedGetAll(dataset):
    
    data = getAll(dataset)
    id = data[]
def formatedGetAllAsFile(dataset):
    pass




if __name__=="__main__":
    # Now wen calling the function to save the contents in a file, we only need to add the dataset name as a function parameter
    # instead of changing the url every time
    getAllFile("FIQ02")