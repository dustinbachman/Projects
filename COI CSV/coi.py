# 8/31/2023
# Main counties and main occupations
# Trying to figure out what kind of person is subscribing to COI
# How many of each general group of jobs 
# Categories: Health related (Practitioner, Physcian, Nurse, Doctor, Health (not mental), DR, RN)
#             Social Work (Case Worker, Social Worker, Caseworker, Social, Care Coordinator, Counselor, Therapist, Psychiatrist, Psychologist, Mental, Foster, Behavioral)
#             Administrative (Director, Facilitator, Coordiantor, Administrative, Assistant, Manager)
#             Specialists (Specialist)
#             Other

# Import
import csv
from collections import Counter

# Categories
health = ['practitioner', 'physician', 'nurse', 'doctor', 'health'] # do rn and dr separately
social = ['case worker', 'social worker', 'caseworker', 'social', 'care coordinator', 'counselor', 'therapy', 'therapist', 'psychiatrist', 'psychologist', 'mental', 'foster', 'behavioral']
admin = ['director', 'facilitator', 'coordinator', 'administrative', 'assistant', 'manager', 'supervisor']
spec = ['specialist']

# output categories 
healthOut = []
socialOut = []
adminOut = []
specOut = []


# other
other = []
spaces = ['', '', '', '', '']

# Popular Words lists
popularOne = []
popularTwo = []
popularThree = []
popularFour = []
popularFive = []
popularSix = []
popularSeven = []
popularEight = []
popularNine = []
popularTen = []

# open 
def openFile():
    # keep track of every job
    global jobs
    jobs = []
    with open('file.csv') as file_obj:
        heading = next(file_obj)
        reader_obj = csv.reader(file_obj)
        for row in reader_obj: 
            # n is counting not empty strings
            n = 1
            # x is keeping track of array location
            x = 0
            # go through each row to find 3rd location with data and save to jobs array
            for i in row: 
                if n == 3:
                    if not(row[x] == ''):
                        jobs.append(i)
                    break
                if not(i == ''):
                    n += 1
                x += 1

# Split the jobs into different categories
def jobSplit(): 

    global jobs

    for i in jobs: 

        # Lowercase to check for jobs
        i = i.lower()

        # Keep track of if current job fits into any categories.
        flag = False
        # check for social
        for j in social: 
            if j in i:
                socialOut.append(i) 
                flag = True

        # check for admin
        for j in admin: 
            if j in i:
                adminOut.append(i) 
                flag = True

        # check for spec
        for j in spec: 
            if j in i:
                specOut.append(i) 
                flag = True

        # check for health
        if i == 'dr' or i == 'rn': 
            healthOut.append(i)
            flag = True
        for j in health: 
            if j in i and not('mental' in i):
                healthOut.append(i) 
                flag = True
        
        # Not found in any other category
        if flag == False: 
            other.append(i)

    # Sort the categories to make output cleaner
    healthOut.sort()
    socialOut.sort()
    adminOut.sort()
    specOut.sort()
    other.sort()

# Find the 10 most popular words
def findPopular(): 

    # Variables
    global popular
    popular = []
    global popularOut
    popularOut = []

    # Combine list into a single string
    i = ' '.join(other)
    s = i.split()
    
    # Use Counter to access the 10 most common words in string
    count = Counter(s)
    popular.append(count.most_common(10))

    # Traverse the tuple to get just the job titles, not the amount
    for i in popular[0]: 
        popularOut.append(i[0])

    # Go through each most popular word one by one and put the full job title into the correct list
    for i in other: 
        if popularOut[0] in i:
            popularOne.append(i) 
        if popularOut[1] in i:
            popularTwo.append(i) 
        if popularOut[2] in i:
            popularThree.append(i) 
        if popularOut[3] in i:
            popularFour.append(i) 
        if popularOut[4] in i:
            popularFive.append(i) 
        if popularOut[5] in i:
            popularSix.append(i) 
        if popularOut[6] in i:
            popularSeven.append(i) 
        if popularOut[7] in i:
            popularEight.append(i) 
        if popularOut[8] in i:
            popularNine.append(i) 
        if popularOut[9] in i:
            popularTen.append(i) 
        
    # Testing
    #print(popularOut)



# How many of each, most popular words in other, list separated into categories
def csvOut(): 
    # Start of the header

    headerOne = ['', 'Health', '', '', '', '', '', 'Social', '', '', '', '', '', 'Administrative', '', '', '', '', '', 'Specialist', '', '', '', '', '', 'Other', '', '', '', '', '', 'Most popular words in \'other\'']
    # Start of line two
    lineTwo = ['Num: ', str(len(healthOut)), '', '', '', '', '', str(len(socialOut)), '', '', '', '', '', str(len(adminOut)), '', '', '', '', '', str(len(specOut)), '', '', '', '', '', str(len(other)), '', '', '', '', '', '', '', '', '', '', '']
    
    # Find the biggest number in a single category to keep track of how many lines are needed
    max = 0
    if max < len(healthOut):
        max = len(healthOut)
    if max < len(socialOut):
        max = len(socialOut)
    if max < len(adminOut):
        max = len(adminOut)
    if max < len(specOut):
        max = len(specOut)
    if max < len(popularOut):
        max = len(popularOut)
    if max < len(other):
        max = len(other)

    # Create the headers for the most popular words 
    popHeader = ['', '', '', '', '']
    x = 0
    for i in popularOut: 
        # Append the popular word, and the amount that it is found underneath it
        popHeader.append(i)
        lineTwo.append(popular[0][x][1])
        for i in range (5):
            popHeader.append('')
            lineTwo.append('')
        x += 1

    # Combine the start of the header with the popular words
    header = headerOne + popHeader

    # Open the CSV file to write
    with open('output.csv', 'w', newline='') as csvfile:
        
        # Begin to write to the file
        csvwriter = csv.writer(csvfile)

        # Write the header and second line with numbers
        csvwriter.writerow(header)
        csvwriter.writerow(lineTwo)

        # For max amount, print each column
        for x in range(max):
            o = ['']
            if x < len(healthOut):
                o.append(healthOut[x])
            else: 
                o.append('')
            for i in range (5):
                o.append('')
            if x < len(socialOut):
                o.append(socialOut[x])
            else: 
                o.append('')
            for i in range (5):
                o.append('')
            if x < len(adminOut):
                o.append(adminOut[x])
            else: 
                o.append('')
            for i in range (5):
                o.append('')
            if x < len(specOut):
                o.append(specOut[x])
            else: 
                o.append('')
            for i in range (5):
                o.append('')
            if x < len(other):
                o.append(other[x])
            else: 
                o.append('')
            for i in range (5):
                o.append('')
            if x < len(popularOut):
                o.append(popularOut[x])
            else: 
                o.append('')
            for i in range (5):
                o.append('')
            if x < len(popularOne):
                o.append(popularOne[x])
            else: 
                o.append('')
            for i in range (5):
                o.append('')
            if x < len(popularTwo):
                o.append(popularTwo[x])
            else: 
                o.append('')
            for i in range (5):
                o.append('')
            if x < len(popularThree):
                o.append(popularThree[x])
            else: 
                o.append('')
            for i in range (5):
                o.append('')
            if x < len(popularFour):
                o.append(popularFour[x])
            else: 
                o.append('')
            for i in range (5):
                o.append('')
            if x < len(popularFive):
                o.append(popularFive[x])
            else: 
                o.append('')
            for i in range (5):
                o.append('')
            if x < len(popularSix):
                o.append(popularSix[x])
            else: 
                o.append('')
            for i in range (5):
                o.append('')
            if x < len(popularSeven):
                o.append(popularSeven[x])
            else: 
                o.append('')
            for i in range (5):
                o.append('')
            if x < len(popularEight):
                o.append(popularEight[x])
            else: 
                o.append('')
            for i in range (5):
                o.append('')
            if x < len(popularNine):
                o.append(popularNine[x])
            else: 
                o.append('')
            for i in range (5):
                o.append('')
            if x < len(popularTen):
                o.append(popularTen[x])
            else: 
                o.append('')
            for i in range (5):
                o.append('')
            csvwriter.writerow(o)

        

        
# Need to open the file first
openFile()
jobSplit()
findPopular()
csvOut()