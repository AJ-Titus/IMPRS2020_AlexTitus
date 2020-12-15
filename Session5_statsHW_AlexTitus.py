  
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import plotnine as gg
import os

#I used the "lexical decision" repository because I only had one CSV result of my own.)
#load the data
results = pd.read_csv('session5\lexdec_results.csv')  # Let's load in our participant data!
#print(results)

#change the name of the first column name
results.rename(columns={'Unnamed: 0': 'trial_order'}, inplace=True)

# Create a list of conditions
conditions = [
    results['frequency'].str.startswith('NW'),
    results['frequency'].str.startswith('LF'),
    results['frequency'].str.startswith('HF')
]

# Create a list of values we want to assign to each condition
values = ['NW', 'LF', 'HF']

# Create a new column and assign values to the conditions
results['condition'] = np.select(conditions, values)
#print(results)

# Make dataset of summary stats
summary = results.groupby(by = 'condition').aggregate(
    mean_RT = pd.NamedAgg('reaction_time', np.mean),
    std_RT = pd.NamedAgg('reaction_time', np.std),
)
summary.reset_index(inplace = True)
#print(summary)

#visualize the date in a few ways
#Raw data
###### RTs
sns.catplot(x="frequency", y= "reaction_time", kind = "box", data=results)
plt.suptitle("Boxplot of reaction times as a function of word frequency.")
plt.savefig('catplot.png')

#desity plot: distribution of mean reaction times as a function of word frequency
sns.displot(results, x="reaction_time", hue="frequency", kind="kde", fill=True)
plt.suptitle("Reaction times as a function of word frequency.")
plt.savefig('desity_plot.png')

histogram = sns.catplot(data = results, kind = 'bar', x = 'condition', y = 'reaction_time', ci = 'sd')
histogram.set_axis_labels('', 'Reaction time (s)')
plt.savefig('histogram.png')