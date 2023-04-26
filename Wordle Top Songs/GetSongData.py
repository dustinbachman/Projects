# Dustin Bachman
# Last Updated 8 April 2023
# Purpose: Guess the year based on the top 3 songs on the Billboard Hot 100.
# Start with #5, points based on how early they place the guess and get it right

# Import statements
import random # Used to generate year
import datetime # Used to get current year
from lxml import html # Used to scrape data
import requests # Used to scrape data
import tkinter # Used for GUI
import re # Used for YT link
from youtubesearchpython import VideosSearch
import pafy
import vlc

# Variables 
maxYear = datetime.date.today().year
minYear = 1958
usedYears = [] # [year - minYear]
songs = [] # hold the top 5 songs of every year, [year-minYear]
artists = [] # holds the artist for the top 5 songs of each year
ytLinks = [] # holds the youtube links to the songs
currentNum = 0
numOfSongs = 5
userCorrect = False

# Set up variable
# # usedYears
def clearUsedYears():
    for i in range(0, maxYear-minYear):
        usedYears.append(False)

# Get Random Year
def getYear(): 
    print('Generating a year...')
    y = random.randint(1958, maxYear)
    # Make sure year has not been used
    while (y in usedYears):
        y = random.randint(1958, maxYear)
    usedYears[y-minYear] = True
    global year
    year = str(y)


def genYTLink(s, a): 
    term = s + ' ' + a
    ytSearch = VideosSearch(term, limit = 1)
    ytLink = ytSearch.result()['result'][0]['link']
    ytLinks.append(ytLink)


def scrapeData(): # FIXME: Change back to only downlaod data currently being used, possibly output to xml file on first opening?
    global musicLink
    global data
    musicLink = 'http://billboardtop100of.com/' + year + '-2/'
    page = requests.get(musicLink)
    tree = html.fromstring(page.content)
    data = tree.xpath('//td/text()') 
    print('Downloading Billboard Data...') # Let the user know what is happening
    # clear the lists
    songs.clear()
    artists.clear()
    ytLinks.clear()
    count = 1
    # Save top 5 songs and artists
    for j in range(15):
            if count == 2:
                artists.append(data[j])
            if count == 3:
                songs.append(data[j])
                count = 0
            count = count + 1
    for j in range(len(songs)):
            genYTLink(songs[j], artists[j])

def gameplay():
    currentNum = numOfSongs
    userGuess = 0
    while (userCorrect == False):   
        print('Number ' + (str(currentNum)) + ' song of the year: '+ songs[numOfSongs-currentNum] + ' by ' + artists[numOfSongs-currentNum])
        userGuess = int(input('Guess the year ('+ str(minYear) + '-'+ str(maxYear-1) + '):'))
        if (userGuess >= maxYear or userGuess < minYear):
            print('Error: Please enter a year between ' + str(minYear) + ' and ' + str(maxYear))
            continue
        if (userGuess == int(year)):
            print('Correct!')
            break
        if(userGuess > int(year)):
            print('Incorrect, older.')
        else:
            print('Incorrect, more recent.')
        currentNum = currentNum - 1
        if (currentNum == 0):
            ('Sorry! The correct answer is: ' + year)

# Get User Input on what to do
#userNum = int(input('Please enter: 0 to download new data, or anything else to use already downloaded data '))

# Setup
clearUsedYears() # set up the used years array
getYear()
scrapeData()
gameplay()


uIn = int(input("Press 1 to play again, 0 to quit: "))
while (uIn != 0):
     print(usedYears[int(year)-minYear])
     getYear()
     scrapeData()
     gameplay()
     uIn = int(input("Press 1 to play again, 0 to quit: "))
    

# Testing
print(year)
for i in range(len(songs)):
        print(songs[i] + ' - ' + artists[i])
#openYTLink(ytLinks[0])2016