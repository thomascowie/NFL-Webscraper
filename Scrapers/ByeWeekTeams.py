
#Bye Week Web Scraper
import requests
from bs4 import BeautifulSoup

URL = "https://www.fantasypros.com/nfl/bye-weeks.php"
page = requests.get(URL)  # Getting the Page

soup = BeautifulSoup(page.content, "html.parser")  # Parsing as HTML

#Get Teams
teams = soup.find_all(
    "tr", class_="sport-schedule__tr")

#Strip Text
teamList = []
for team in teams:
    team = teams.find(
        "a", class_="sport-schedule__link")
    teamList.append(team.text)

#Get Bye Weeks
byeWeeks = soup.find_all(
    "td", class_="sport-schedule__td sport-schedule__bye-column")

#Strip Week Number
byeList = []
for week in byeWeeks:
    week = byeWeeks.find(
    "a", class_="sport-schedule__link")
    byeList.append(week.text)

for team, week in zip(teamList, byeList):
    print(team + " : " + week)

#To fix I need to look at the elements and find it in another order.