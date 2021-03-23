"""
This script is used to produce the plots which accompany the submission.
"""

import pandas as pd

name = 'Histogram of Number Training Examples to Learn Target Concept'

df = pd.read_csv('experimental_question.csv', header=None).transpose()
df.columns = [name]

hist = df.hist([name], bins=df[name].nunique())

fig = hist[0][0].get_figure()

fig.savefig('experimental_question.png')