# First we'll import the os module 
# This will allow us to create file paths across operating systems
import os
import csv
#import pandas as pd

csvpath = os.path.join('budget_data_1.csv')

# Improved Reading using CSV module
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    num_cols = 0
    #  Each row is read as a row
    for row in csvreader:
        # print(row)
        num_cols = num_cols + 1
        print(num_cols)

        




