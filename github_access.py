import tmp
from github import Github

# personal access token
name = "flora-m"
token = tmp.getToken()
g = Github(token)
user = g.get_user()


def generateData(repoAddress, graphData):
    # create child for repo
    child = {
        "name": repoAddress,
        "children": getRepoData(repoAddress)
    }
    # append repo to overall data
    graphData["children"].append(child)
