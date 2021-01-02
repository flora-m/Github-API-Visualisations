from flask import Flask, render_template
from collections import defaultdict, OrderedDict
import collections
import sys
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("homePage.html")


def handleInput(repos, repo):
    if (repo):
        repos.append(repo)

