import csv # to export
import requests # for scraping 
from lxml import html # for scraping 

# Scrapes ESPN for current score data and saves it to CSV
def updateData():
    if (int(week) > 18):
        address = 'https://www.espn.com/nfl/scoreboard/_/week/'+ str(postWeek) + '/year/'+ year + '/seasontype/3'
    else:
        address = 'https://www.espn.com/nfl/scoreboard/_/week/' + week + '/year/' + year + '/seasontype/2'
    address = 'https://letterboxd.com/films/decade/2020s/genre/horror/by/rating/'
    page = requests.get(address)
    tree = html.fromstring(page.content)
    global scores
    global teams
    # Get info from HTML
    #<a href="/film/eternally/" class="frame" title="Eternally (2020) 4.27"><span class="frame-title">Eternally (2020)</span><span class="overlay"></span></a>
    movies = tree.xpath('//div[@class="title"]/text()')
    size = len(scores)
    global gameList
    gameList = []
    # Read the games and scores into Games class
    for x in range(0, size, 2):
        p1 = Games(teams[x], scores[x], teams[x+1], scores[x+1])
        gameList.append(p1)
    f = open(ex, 'w+', newline = '',)
    writer = csv.writer(f)
    # Store scraped inputs into game list and write to csv file
    for x in range(len(gameList)):
        team1Name = gameList[x].t1
        team2Name = gameList[x].t2
        team1Score = gameList[x].t1F
        team2Score = gameList[x].t2F
        gameData = [team1Name, team1Score, team2Name, team2Score]
        writer.writerow(gameData)
    f.close()
