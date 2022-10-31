import json

filename = "coindeskprices.json"

# Opening and Reading the file
with open(filename, "r") as fp:
    jsonObject = json.load(fp)

# Getting the Euro rates
euroObject = jsonObject["bpi"]["EUR"]
euroRate = euroObject["rate"]

print(euroObject["code"], euroRate)