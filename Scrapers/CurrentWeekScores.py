import requests
from bs4 import BeautifulSoup

# NFL Scores on ESPN
URL = "https://www.espn.com/nfl/scoreboard"
page = requests.get(URL)  # Getting the Page

soup = BeautifulSoup(page.content, "html.parser")  # Parsing as HTML

# Find all the scores
competitorCards = soup.find_all(
    "ul", class_="ScoreboardScoreCell__Competitors")

# Find the Team Names
teamNames = soup.find_all(
    "div", class_="ScoreCell__Team ScoreCell__Team--scoreboard flex-column pr2")

# Extract Team Name Strings from HTML Tags
team_list = []
for teamName in teamNames:
    team = teamName.find(
        "div", class_="ScoreCell__TeamName ScoreCell__TeamName--shortDisplayName truncate db")
    team_list.append(team.text)

# Extract Score Strings from HTML Tags
score_list = []
for competitorCard in competitorCards:
    # There are 2 of the below classes so we have to find all again and then iterate.
    scores = competitorCard.find_all(
        "div", class_="ScoreCell__Score h4 clr-gray-01 fw-heavy tar ScoreCell_Score--scoreboard pl2")
    for score in scores:
        score_list.append(score.text)

# Fancy Scores
for team, score in zip(team_list, score_list):
    print(team + " : " + score)
