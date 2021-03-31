"""
Vihan Patel, Suada Demirovic, Luke Kurlandski
March 2021

This script is used to produce the plots which accompany the submission.

Note that this script uses the third party library pandas, but that was
	specified as being acceptable by Dr. Bloodgood. Requires the 
	experiment_results.csv file to exist and be formatted as
	a single line of comma-separated values. Produces a .csv and .png 
	file. 

Run this program from the command line like

    > python3 get_plot_and_stats.py

"""

import csv
import pandas as pd
import os
import sys

#TODO: Add code to label the x and y axes for the histogram.

#check if experiment_results.csv exists
value = os.path.exists("experiment_results.csv")

if(value == False):
    print()
    print('The file, experiment_results.csv, does not exist.')
    print('Please run experiment.py.')
    print()
    sys.exit(0)
#

# Get the produced data.
df = pd.read_csv('experiment_results.csv', header=None).transpose()
name = 'Histogram of Number Training Examples to Learn Target Concept\nn_trials=' + str(len(df.index))
df.columns = [name]

# Produce an image and save it to a .png file.
hist = df.hist([name], bins=df[name].nunique())
fig = hist[0][0].get_figure()
fig.savefig('histogram.png')

# Record statistical information in a .csv file.
details = {
	"n" : len(df.index),
	"min" : df[name].min(),
	"max" : df[name].max(),
	"mode" : str(df[name].mode().to_list())[1:][:-1],
	"mean" : df[name].mean(),
	"stnd dev" : df[name].std(),
	"median" : df[name].median()
}

with open('statistics.csv', 'w') as f:  # You will need 'wb' mode in Python 2.x
    w = csv.DictWriter(f, details.keys())
    w.writeheader()
    w.writerow(details)
