import tmp
from github import Github

name = "flora-m"
token = tmp.getToken()
g = Github(token)

for repo in g.get_user().get_repos():
    print("{0:80} Language: {1:80}".format(str(repo), str(repo.language)))