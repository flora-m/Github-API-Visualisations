from flask import Flask, request, render_template, jsonify
from collections import defaultdict, OrderedDict
import collections
import sys
import json
from get_json import generateData

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("homePage.html")


@app.route("/graph", methods = ['POST'])
def index2():
    repos = []
    handleInput(repos, request.form['repo1'])
    handleInput(repos, request.form['repo2'])
    handleInput(repos, request.form['repo3'])
    handleInput(repos, request.form['repo4'])
    handleInput(repos, request.form['repo5'])
    print(repos)
    generateData(repos)
    graph = createGraph()
    return render_template("graphPage.html", graph = graph)


def handleInput(repos, repo):
    if (repo):
        repos.append(repo)


def readInFile(filename):
    with open(filename) as json_file:
        return json.load(json_file)


def createGraph():
    graph = readInFile("data.json")
    return graph


