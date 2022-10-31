from urllib import response
import requests
import urllib.parse
# Importing the Api key saved in config to protect the key
from config import config as cfg


target_url = "https://en.wikipedia.org"
api_key = cfg["html2pdf"]
api_url = "https://api.html2pdf.app/v1/generate"


#These paramenters names(the names have to be exact the same) can be found at https://html2pdf.app/documentation/
params = {"url":target_url, "apiKey":api_key}
parsed_params = urllib.parse.urlencode(params)

# Api url + the parameters(Target url and Api key), this can be found in the documentation
request_url = api_url + "?" + parsed_params


# Sendig a "Get" to get back the information from the page
response_url = requests.get(request_url)
#And printing the status code to see if the request was successful
print(response_url.status_code)

result = response_url.content

#Saving contents in a file

with open("document.pdf", "wb") as file:
    file.write(result)
