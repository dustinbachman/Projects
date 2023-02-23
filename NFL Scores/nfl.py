# Scrape NFL scores, get input and export to CSV file. Compare CSV file to scraped values and evaluate winner.
# Dustin Bachman
# 20 November 2022
# 

import csv # to export
import requests # for scraping 
from lxml import html # for scraping 

# class to store games in
class Games:
    def __init__(self, team1, team1Final, team2, team2Final):
        self.t1 = team1
        self.t1F = team1Final
        self.t2 = team2
        self.t2F = team2Final

# Get input for the date
def getDateInput(): 
    # Get input for the season/year
    global year
    print('Which season?')
    print('1. 21/22')
    print('2. 22/23')
    flag = False
    y = ''
    # Loops until correct value is obtained
    while (flag == False):
        print()
        y = int(input())
        print()
        if (y != 1 and y != 2):
            print("Error: Value needs to be 1 or 2")
            continue
        flag = True
    # Save to year
    if (y == 1):
        year = '2021'
    elif (y == 2):
        year = '2022'
    # Get input for the week
    global week
    print('1. Regular Season or 2. Post?')
    print()
    s = int(input())
    print()
    # If Post-Season
    if (s == 2):
        print('Which game?')
        print('1. Wild Card Weekend')
        print('2. Divisional Playoffs')
        print('3. Conference Championships')
        print('4. Pro Bowl')
        print('5. Super Bowl')
        global postWeek
        flag = False
        while(flag == False):
            print()
            postWeek = int(input())
            print()
            if (postWeek < 1 or postWeek > 5):
                print("Error: Value needs to be between 1 and 5, inclusive")
                continue
            flag = True
        match postWeek:
            case 1:
                week = '19'
            case 2:
                week = '20'
            case 3:
                week = '21'
            case 4: 
                week = '22'
            case 5:
                week = '23'
    # If Regular Season
    else:
        print('Which week?')
        flag = False
        w = ''
        while (flag == False):
            print()
            w = input()
            if(int(w) < 1 or int(w) > 18):
                print("Error: Value needs to be between 1 and 23, inclusive")
                continue
            flag = True
        week = w
    global pickFile
    pickFile = 'Picks/' + year + '_Week_Picks_' + week + '.csv'
    print()

# Adds a player to the selected CSV
def addPlayer():
    updateData()
    gameList = getGameData()
    flag = False
    print('Name?')
    global name
    print()
    name = input()
    print()
    rowData = [name]
    # Ask for input for each game
    for x in gameList: 
        print('1. ' + x.t1 + ' vs 2. ' + x.t2)
        print()
        n = int(input())
        print()
        while( n != 1 and n != 2):
            print("Error: Please select either 1 or 2")
            n = int(input())
        if (n == 1):
            u = x.t1
        else:
            u = x.t2
        rowData.append(u)
    print("Monday night total?")
    monTotal = input()
    rowData.append(monTotal)
    # Open and write to the file
    f = open(pickFile, 'a+', newline = '',)
    writer = csv.writer(f)
    writer.writerow(rowData)
    f.close()
    print()


# Puts all the names of players into a list
def getNames():
    global nameList
    nameList = []
    with open(pickFile) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        for row in csv_reader:
            nameList.append(row[0])
    return nameList

# Checks the scores of the games
def checkGameScores():
    updateData()
    gameList = getGameData()
    for x in gameList:
        if (int(x.t1F) > int(x.t2F)):
            print('%-15s%3s <' % (x.t1, x.t1F))
            print('%-15s%3s' % (x.t2, x.t2F))
        else:
            print('%-15s%3s' % (x.t1, x.t1F))
            print('%-15s%3s <' % (x.t2, x.t2F))
        print()

# Get name input
def chooseName():
    nameList = getNames()
    print("From who?: ")
    # Print out all possible choices
    for x in range(len(nameList)):
        print(str(x + 1) + '. ' + nameList[x])
    print()
    p = int(input())
    print()
    global picked
    # p - 1 because indices start at 0 while list starts at 1
    picked = nameList[p - 1]


# Puts player's picks into a list
def getPicks():
    pickedList = []
    with open(pickFile) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        for row in csv_reader:
            if (row[0] == picked):
                for x in range(1, len(row) - 1):
                    pickedList.append(row[x])
    return pickedList


# Prints out the picks of a player
def printPicks():
    pickedList = getPicks()
    for x in pickedList:
        print(x)


# Compares the picks of a player to the results
def compare():
    updateData()
    pickedList = getPicks()
    actualScores = getGameData()
    winners = []
    for x in actualScores: 
        if ( x.t1F > x.t2F ):
            winners.append(x.t1)
        else:
            winners.append(x.t2)
    wCount = 0
    for x in range(len(pickedList)):
        if (pickedList[x] in winners):
            wCount = wCount + 1
    return wCount


# Shows the score of a specific player
def showScore():
    count = compare()
    print(picked, count)


# Displays the scores of all the players
def getAllScores():
    nameList = getNames()
    for x in nameList:
        global picked 
        picked = x
        showScore()


# Displays the overall winner
def showWinner(): 
    updateData()
    nameList = getNames()
    currWinner = ''
    currMax = 0
    winnerList = []
    # Go through list checking for highest num
    for x in nameList: 
        global picked 
        picked = x
        n = compare()
        # Higher score was found
        if (n > currMax):
            currMax = n
            currWinner = x
            # New winner was found, clear list
            winnerList.clear()
        # There is more than one winner
        elif (n == currMax):
            if (not(currWinner in winnerList)):
                winnerList.append(currWinner)
            winnerList.append(x)
    # Checks if there was more than one winner
    if (len(winnerList) != 0):
        print("Score: " + str(currMax))
        for x in winnerList:
            print(x)
    else:
        print(currWinner + ' ' + str(currMax))
        

# Retrieves game data from file
def getGameData():
    with open(ex) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        global gameList
        gameList = []
        for row in csv_reader:
            p1 = Games(row[0], row[1], row[2], row[3])
            gameList.append(p1)
        return gameList
            

# Scrapes ESPN for current score data and saves it to CSV
def updateData():
    if (int(week) > 18):
        address = 'https://www.espn.com/nfl/scoreboard/_/week/'+ str(postWeek) + '/year/'+ year + '/seasontype/3'
    else:
        address = 'https://www.espn.com/nfl/scoreboard/_/week/' + week + '/year/' + year + '/seasontype/2'
    page = requests.get(address)
    tree = html.fromstring(page.content)
    global scores
    global teams
    # Get info from HTML
    scores = tree.xpath('//div[@class="ScoreCell__Score h4 clr-gray-01 fw-heavy tar ScoreCell_Score--scoreboard pl2"]/text()')
    teams = tree.xpath('//div[@class="ScoreCell__TeamName ScoreCell__TeamName--shortDisplayName truncate db"]/text()')
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

# Main function for applicaton
def main():
    flag = False
    x = 0
    # Get input for day
    getDateInput()
    # Get the export file name
    global ex
    ex = 'Games/' + year + '_Week_' + week + '.csv'
    while(flag == False):
        # Print out options
        print("1. Add new player \n2. Retrieve new game data \n3. Check Picks \n4. Check Pick Score \n5. Check All Pick Scores \n6. Check Winner \n7. Check Game Scores\n8. Quit")
        print()
        x = input()
        print()
        # Data validation
        if (int(x) < 1 or int(x) > 8):
            print("Error: Needs to be 1-8")
            continue
        # Choose user inputted option
        match int(x):
            case 1:
                addPlayer()
                print()
                continue
            case 2:
                updateData()
                print()
                continue
            case 3:
                chooseName()
                printPicks()
                print()
                continue
            case 4:
                chooseName()
                showScore()
                print()
                continue
            case 5:
                getAllScores()
                print()
                continue
            case 6:
                showWinner()
                print()
                continue
            case 7:
                checkGameScores()
                print()
            case 8:
                flag = True
            
# Call main function to begin
main()