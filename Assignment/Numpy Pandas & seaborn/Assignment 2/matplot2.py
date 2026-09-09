print("hello");
import seaborn as sns
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

data = pd.DataFrame({'x': np.arange(100), 'y': np.random.rand(100).cumsum()})

#set the theme
sns.set_theme(style='darkgrid')

# create plot
sns.lineplot(x='x',y='y',data=data)
plt.show()
# Customize the theme
sns.set_theme(style='darkgrid', rc={'axes.facecolor': 'grey', 'grid.color': 'white'})

# Create a plot
sns.displot(x='x', y='y', data=data)
plt.show()

df=pd.read_csv("Plot 2/Real_Estate_Sales_2001-2022_GL-Short.csv",delimiter=',',na_filter=False)
print(df)
dffilter=df.head(50)
print(dffilter)
sns.set_theme(style='darkgrid')
g=sns.countplot(x='Town',data=dffilter)
plt.show()

a=sns.scatterplot(x='Assessed Value',y='Sale Amount',data=dffilter)
plt.show()

warm=dffilter.pivot(columns='Assessed Value',values='Sale Amount')
g=sns.heatmap(warm)
g.figure.suptitle("My Heat Map title")
plt.show()

cold=sns.set_theme(style="ticks")


# Show the results of a linear regression within each dataset
sns.lmplot(
    data=df, x="Address", y="Town", col="Sale Amount", hue="Sale Ratio",
    col_wrap=2, palette="muted", ci=None,
    height=4, scatter_kws={"s": 50, "alpha": 1}
)