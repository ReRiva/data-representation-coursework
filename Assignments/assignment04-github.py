from github import Github
import requests
from config import github as gtb
import pandas as pd

api_key = gtb["github"]
git = Github(api_key)

# Getting the repository
repo = git.get_repo("Reriva/privaterepo1")

#print(repo.clone_url)
file_info = repo.get_contents("Assign.txt")

# Url from the file, so we can access it
file_url = file_info.download_url

#Printing to check if the link is ok
#print (file_url)

response = requests.get(file_url)
file_contents = response.text

# Replacing the text inside the file
origial_text = "Andrew"
replace_text = "Renan"

with open("Assign.txt", "w") as file:
    file.write(file_contents)
with open("Assign.txt", "r") as file:
    data = file.read()
    data = data.replace(origial_text, replace_text)
with open("Assign.txt", "w") as file:
    file.write(data)
with open("Assign.txt", "r") as file:
    new_content = file.read()
print(new_content)

# Updating the file on GitHub
git_update = repo.update_file(file_info.path, "Replaced names", new_content, file_info.sha)
print(git_update)
