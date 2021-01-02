import tmp 
from github import Github
import datetime
import json

# personal access token
token = tmp.getToken()
g = Github(token)
user = g.get_user()


def generateData(repos):
    graphData = {
        "name" : "data",
        "children" : []
    }
    # get JSON data structured in a way that matches d3
    structureJSON(repos, graphData)

    # export to data.json file
    with open("data.json", "w") as outfile:
        json.dump(graphData, outfile)


def structureJSON(repos, graphData):
    for repo in repos:
        # create "child" for repo
        child = {
            "name": repo,
            "children": getRepoData(repo)
        }
        # append repo to overall data
        graphData["children"].append(child)


def getRepoData(repoAddress):
        # structure for d3
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

            # check if author has already committed on this weekday
            authors = [x for x in week[weekday]["children"] if x["name"] == str(author)]
           
            # if not, initialise number of commits (size) to 1
            if(not authors):
                week[weekday]["children"].append({"name": str(author), "size": 1})
            
            # if they have already committed, increment number of commits (size) by 1 
            else:
                authorObject = authors[0]
                authorObject["size"] += 1
    
    # check if there are any days with no authors and if there are, set the number of commits (size) equal to 0
    for i in range(7):
        authors = [x for x in week[i]["children"]]
        if(not authors):
            week[i]["children"].append({"name": "No Commits", "size": 0})
    return week