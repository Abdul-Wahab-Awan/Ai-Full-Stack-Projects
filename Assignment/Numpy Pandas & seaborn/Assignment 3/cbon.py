import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#https://seaborn.pydata.org/generated/seaborn.set_theme.html
#https://seaborn.pydata.org/tutorial/aesthetics.html
#https://python-charts.com/seaborn/themes/

"""
 Built-in Themes
Seaborn provides five built-in themes:
darkgrid: Adds a gray background with white gridlines. It is the default theme.
whitegrid: Adds gray gridlines on a white background.
dark: Similar to darkgrid but without the gridlines.
white: Similar to whitegrid but without the gridlines.
ticks: Adds ticks to the axes and uses a white background.
Setting Themes
The seaborn.set_theme() or seaborn.set_style() function can be used to set the theme for all plots. """

# Sample data
data=pd.DataFrame({'city':(100), 'country':np.random.rand(100).cumsum()})

# Set the theme
sns.set_theme(style='darkgrid')
# Alternatively
# sns.set_style('darkgrid')

df = pd.read_csv(r'Hunger\FastFoodRestaurants.csv',delimiter="," )



print(df)
dffilter= df.head(2)


#sns.set(style="whitegrid")

#The relationship between x and y can be shown for different subsets of the data using the hue, size, and style parameters. These parameters control what visual semantics are used to identify the different subsets. It is possible to show up to three dimensions independently by using all three semantic types, but this style of plot can be hard to interpret and is often ineffective. Using redundant semantics (i.e. both hue and style for the same variable) can be helpful for making graphics more accessible."""
g=sns.lineplot(data=dffilter, x="city" , y="country"  )
g.figure.suptitle("sns.lineplot(data=dffilter, x=city , y=country  )"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()

#https://seaborn.pydata.org/generated/seaborn.barplot.html
"""Show point estimates and errors as rectangular bars.

A bar plot represents an aggregate or statistical estimate for a numeric variable with the height of each rectangle and indicates the uncertainty around that estimate using an error bar. Bar plots include 0 in the axis range, and they are a good choice when 0 is a meaningful value for the variable to take."""
