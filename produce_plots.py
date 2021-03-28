"""
This script is used to produce the plots which accompany the submission.
"""

import csv
import pandas as pd

# Get the produced data.
df = pd.read_csv('experimental_question.csv', header=None).transpose()
name = 'Histogram of Number Training Examples to Learn Target Concept'
df.columns = [name]

# Produce an image.
hist = df.hist([name], bins=df[name].nunique())
fig = hist[0][0].get_figure()
fig.savefig('experimental_question.png')

# Record important experimental information in a csv file. Suggested to 
	# open the produced csv file into excel, take a screenshot, and 
	# save it to a pdf along with the png image.

details = {
	"n" : len(df.index),
	"min" : df[name].min(),
	"max" : df[name].max(),
	"mode" : str(df[name].mode().to_list())[1:][:-1],
	"mean" : df[name].mean(),
	"stnd dev" : df[name].std()
}

with open('experimental_details.csv', 'w') as f:  # You will need 'wb' mode in Python 2.x
    w = csv.DictWriter(f, details.keys())
    w.writeheader()
    w.writerow(details)
