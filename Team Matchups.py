# Web Scraping for teams and their matchups.

import requests
from bs4 import BeautifulSoup

# NFL Scores on ESPN
URL = "https://www.espn.com/nfl/scoreboard"
page = requests.get(URL)  # Getting the Page

soup = BeautifulSoup(page.content, "html.parser")  # Parsing as HTML

# Get the team names
teamNames = soup.find_all(
    "div", class_="ScoreCell__Team ScoreCell__Team--scoreboard flex-column pr2")

# Fix the formatting to get rid of the html
team_list = []
for teamName in teamNames:
    team = teamName.find(
        "div", class_="ScoreCell__TeamName ScoreCell__TeamName--shortDisplayName truncate db")
    team_list.append(team.text)

# Print Menu
print("Pick a team to get the schedule for.")
iterator = 1
teamDictionary = {}
for team in team_list:
    print(iterator, '. ', team)
    teamDictionary.update({iterator: team})
    iterator = iterator + 1

print("Team to get schedule from is: ")
inTeam = input().lower()



