# Github-API-Visualisation

# Description
This is a project for the module CSU33012 Software Engineering to visualise data from the Github API.
My project takes up to five repositories from the user and aims to look at trends between day of the week and number of commits.
The program shows the days of the week with their size representing the number of commits in the repository on each given day. It also shows the users active on each weekday.

This project was developed using Python3 and the PyGithub library. Flask was used to connect the backend to the HTML frontend, which displays a graph using the d3 Javascript Library. The JSON files received from the GitHub API were processed to fit the JSON structure d3 requires.

# Prerequisites for Running This Program
  - Python 3 (I used v.3.8.1)
  - PyGithub
  - Flask
  - also uses the d3 Javascript library in HTML files, but that should be fine without any additional installations

# How to Run
  - have required software setup
  - type in terminal: "python -m flask -run"
  - open URL in browser
  - submit repositories to look at and click submit
  - if there are any changes made to the code, press "ctr + C" in terminal to stop program and delete the data.json folder 
  
# Home Page

![](screenshots/homepage.png)

# Graph Page

![](screenshots/graphPage.png)

# Demonstration GIF

![](screenshots/weekday_popularity.gif)

note: the GIF has been sped up to make demonstration smoother
