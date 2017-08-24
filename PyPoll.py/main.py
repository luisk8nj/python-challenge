
# First we'll import the os module 
# This will allow us to create file paths across operating systems
import os
import csv
csvpath = os.path.join('election_data_1.csv')

# Improved Reading using CSV module
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=';')

    #  Each row is read as a row
    for row in csvreader:
        # print(row)
        print(row[0])