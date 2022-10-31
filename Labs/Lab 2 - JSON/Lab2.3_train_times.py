# Importing the modules

import requests
import csv
from xml.dom.minidom import parseString

#List of tags to be retrieved
retriveTags = ['TrainStatus',
'TrainLatitude',
'TrainLongitude',
'TrainCode',
'TrainDate',
'PublicMessage',
'Direction']



url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)
document = parseString(page.content)

# Checking if it was parsed correctly
#print(document.toprettyxml(), end="")

# Saving the content of the page in a xml file
#with open("train.xml", "w") as xmlfp:
#    document.writexml(xmlfp)

#Getting all the information inside the Parent node "objTrainPositions" 
objTrainPositionsNodes = document.getElementsByTagName("objTrainPositions")

# Storing inside a CSV file
with open("Lab_2.3_trains.csv", mode="w", newline="") as train_file:
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)


    # Getting the train code for each item inside "objTrainPositionsNodes"
    for objTrainPositionsNode in objTrainPositionsNodes:
        trainCodeNode= objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
        trainCode = trainCodeNode.firstChild.nodeValue.strip()
        
        #Creating and appending an array with all the train codes and then writing it to the csv file(train_writer)
        dataList = []
        # Printing only train codes that stars with the letter D
        if trainCode.startswith("D")== True:
            for retriveTag in retriveTags:
                datanode = objTrainPositionsNode.getElementsByTagName(retriveTag).item(0)
                dataList.append(datanode.firstChild.nodeValue.strip())
            train_writer.writerow(dataList)


