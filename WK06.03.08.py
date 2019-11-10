import requests
from github import Github
# remove the minus sign from the key
g = Github("7829ba014c62b61682e14b4df56a62925dbcea71 ")

#for repo in g.get_user().get_repos():
# print(repo.name)

repo = g.get_repo("MKelly1303/52957_Repository_testing")
print(repo.clone_url)

fileInfo = repo.get_contents("README.md")
urlOfFile = fileInfo.download_url
print (urlOfFile)

response = requests.get(urlOfFile)
contentOfFile = response.text
print (contentOfFile)

newContents = contentOfFile + " more stuff \n"
print (newContents)

