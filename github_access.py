import tmp 
from github import Github
import datetime
import json

# personal access token
# name = "flora-m"
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


def getRepoData(repoAddress):
        week = [
            {
                "name": "MONDAY",
                "children": []
            },
            {
                "name": "TUESDAY",
                "children": []
            },
            {
                "name": "WEDNESDAY",
                "children": []
            },
            {
                "name": "THURSDAY",
                "children": []
            },
            {
                "name": "FRIDAY",
                "children": []
            },
            {
                "name": "SATURDAY",
                "children": []
            },
            {
                "name": "SUNDAY",
                "children": []
            }
    ]

    repo = g.get_repo(repoAddress)
    # get commits from repo (only master/main branch)
    commits = repo.get_commits()
    for commit in commits:
        if commit.commit is not None:
            weekday = (commit.commit.author.date).weekday()
            author = commit.commit.author.name

            authors = [x for x in week[weekday]["children"] if x["name"] == str(author)]
            if(not authors):
                week[weekday]["children"].append({"name": str(author), "value": 1})
            else:
                authorObject = authors[0]
                authorObject["value"] += 1
    
    return week


def main():
    graphData = {
        "name" : "data",
        "children" : []
    }
    generateData("nating/cs-exams", graphData)
    
    # export data to data.json file
    with open('data.json', 'w') as outfile:
        json.dump(graphData, outfile)


if __name__ == "__main__":
    # execute only if run as a script
    main()