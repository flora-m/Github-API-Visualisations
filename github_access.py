import tmp
from github import Github

name = "flora-m"
token = tmp.getToken()
g = Github(token)
user = g.get_user()

def(generateData(repoAddress, graphData))