from github import Github
# remove the minus sign from the key
g = Github("7829ba014c62b61682e14b4df56a62925dbcea71 ")
for repo in g.get_user().get_repos():
 print(repo.name)


