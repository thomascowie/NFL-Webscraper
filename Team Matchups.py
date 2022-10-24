#Web Scraping for teams and their matchups.

import requests

# NFL Scores on ESPN
URL = "https://www.espn.com/nfl/scoreboard"
page = requests.get(URL)  # Getting the Page

soup = BeautifulSoup(page.content, "html.parser")  # Parsing as HTML

#Get the team names
teamNames = soup.find_all(
    "div", class_="ScoreCell__Team ScoreCell__Team--scoreboard flex-column pr2")

print("Pick a team to get the schedule for.")
iterator = 1
for team in teamNames:
    print(iterator + '. ' + team + " : " + team)







