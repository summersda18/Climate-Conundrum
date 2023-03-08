# Takes a climate data csv from the web scraping script and converts it into
# a json file that can be easily imported.

# After running this script, use the following command to import the data:
# 'python3 manage.py loaddata convertedData.json'

# Pro tip: The above not work if the json filename is different or is not in
# the same directory as manage.py!

# NOTE: YOU MUST CHANGE THE STARTING INTEGER FOR PRIMARY_KEY IF THERE IS 
#       ALREADY CLIMATE DATA IN THE DATABASE. 

import json
import csv
import datetime

# CSV goes in and JSON comes out.
csvName  = "climateData.csv"
jsonFile = open('convertedData.json', 'w')

# PRIMARY_KEY is the NEXT available climatefactor PK in the database
# dict is where the climatefactor objects will be held until written out
# calendar is just there to make a line shorter later on
PRIMARY_KEY = 138
dict = []


with open(csvName, newline='') as infile:
  lines = csv.reader(infile, delimiter=',', quotechar='|')
  next(lines)
  for line in lines:
    # We are only using one value per month as-is.
    date_unformatted = line[5] + '-' + line[4] + '-01'
    date = (datetime.datetime
            .strptime(date_unformatted, '%Y-%B-%d')
            .strftime('%Y-%m-%d'))

    latitude  = line[0][0:-3]
    longitude = line[1][0:-3]
    city      = line[2]
    state     = line[3]
    maxTemp   = line[6]
    avgTemp   = line[7]
    minTemp   = line[8]
    avgRain   = line[9]
    avgWind   = line[10]

    dict.append({
                  'model': 'website.dateandlocation',
                  'pk': PRIMARY_KEY,
                  'fields': {
                    'date': date,
                    'latitude': latitude,
                    'longitude': longitude,
                    'city': city,
                    'state': state
                  }
                })
    dict.append({
                  'model': 'website.climatefactor',
                  'pk': PRIMARY_KEY,
                  'fields': {
                    'maxTemp': maxTemp,
                    'minTemp': minTemp,
                    'avgTemp': avgTemp,
                    'avgWindSpeed': avgWind,
                    'avgPrecipitation': avgRain,
                    'date': PRIMARY_KEY
                  }
                })

    PRIMARY_KEY += 1

json.dump(dict, jsonFile, indent=2)