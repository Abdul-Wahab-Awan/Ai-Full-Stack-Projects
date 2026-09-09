import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import ExtraTreesClassifier, RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

# CSV File Loaded
df = pd.read_csv('saleforce/Salesforce (CRM) From 2004 To Dec-2024.csv')

print("\nFirst 5 rows:")
print(df.head())

print("\nData Types:")
print(df.dtypes)

# Date column cleaning & Indexing
df['Date'] = pd.to_datetime(df['Date'].str.split(' ').str[0])
print("DAte Col: ",df['Date'])

df = df.sort_values('Date').reset_index(drop=True)
df.set_index('Date', inplace=True)


# # now its time to move to some statical ops 
#
# here we  use describe fun

print("stat ops ")

print(df[['Open', 'High', 'Low', 'Close', 'Volume']].describe())

# now we are using pandas datetime feature for the 
# Time based features


df['Year'] = df.index.year
print("Years: ",df['Year'] )

df['Month'] = df.index.month
print("Months: ",df['Month'] )

df['Quarter'] = df.index.quarter
print("Quanters: ",df['Quarter'] )

df['DayOfWeek'] = df.index.dayofweek  
# 0=Monday, 6=Sunday

print("DAys : ",df['DayOfWeek'] )

# Calculating  year wise avg 
# By USing Groupby mean
print(" Year-wise Average Close Price:")

# Calculating mean avg of Close 
print(df.groupby('Year')['Close'].mean().round(2))

# Calculating DAywise wise avg 
# By USing Groupby mean
print("Day-of-Week Average Close Price:")

# Calculating mean avg of Close 
print(df.groupby('DayOfWeek')['Close'].mean().round(2))

# Calculating MOnthswise wise avg 
# By USing Groupby mean
print(" Month-wise Average Close Price:")

# Calculating mean avg of Close 
print(df.groupby('Month')['Close'].mean().round(2))

# here we have clculted summary of num by using describe

# Now we will do np ops for 
# Calculating Returns & Volatility

print(" NUMPY OPERATIONS: ")

# Daily Returns (Percentage change)
# calculating returns daily

df['Daily_Return'] = df['Close'].pct_change()
print("Daily Return: ",df['Daily_Return'])

# CAlculating LOg return from close
# for more precise calcualtion
df['Log_Return'] = np.log(df['Close'] / df['Close'].shift(1))
print("Log return: ",df['Log_Return'])


# calculating cvolatility
volat = df['Log_Return'].std()
print("Volatility: ",volat)


volat_annum = volat * np.sqrt(252)  
# 252 trading days in a year

print("Volatility of per Annual: ",volat_annum)

# calculating in form of percent
print(f"Daily Volatility: {volat:.4f}")
print(f"Annualized Volatility: {volat_annum:.2%}")

# Drawdown Calculation
# For calculating (Maximum loss from peak)

cumulative_returns = np.cumprod(1 + df['Daily_Return'])
print("Cumulative_returns: ",cumulative_returns)

#calculating Maximum Accumulate
max_running = np.maximum.accumulate(cumulative_returns)
print("Maximum Accumulate of cum return: ",max_running)

# Calculating Drawdown down
df['Draw_down'] = (cumulative_returns - max_running) / max_running
print("Draw_Down: ",df['Draw_down'])

# MAximum DrawDown
max_drawdown = df['Draw_down'].min()
print("MAximum DrawDown: ",max_drawdown)

# In percent
print(f" Maximum Drawdown: {max_drawdown:.2%}")

# Multiple timeframe returns

# for 5 days before return
df['Return_5D'] = df['Close'].pct_change(5)
print("REturn 5 days: ",df['Return_5D'])

# for 10 days before return
df['Return_10D'] = df['Close'].pct_change(10)
print("REturn 10 days: ",df['Return_10D'])

# for 10 days before return
df['Return_20D'] = df['Close'].pct_change(20)
print("REturn 20 days: ",df['Return_20D'])

# NOW WE WILL DO FEATURE ENGINEERING

# Here we will do Such ops 
# 1. Moving Averages 
# 2. Momentum Signal
# 3. Volatility & Liquidity Factors
# 4. Relative Strength Index 
# 5. Moving Average Convergence Divergence 
# 6. Bollinger Bands

# Start from MA (Moving Averages)
# Trend Factors

# For calculating the moving average of close price of last 20 day 
df['MA20'] = df['Close'].rolling(20, min_periods=1).mean()
print("Moving Average of Close price last 20 Days ",df['MA20'])

# For calculating the moving average of close price of last 50 day 
df['MA50'] = df['Close'].rolling(50, min_periods=1).mean()
print("Moving Average of Close price last 50 Days ",df['MA50'])

# For calculating the moving average of close price of last 200 day 
df['MA200'] = df['Close'].rolling(200, min_periods=1).mean()
print("Moving Average of Close price last 200 Days ",df['MA200'])

# for calculating Momentum Signals
#(Price Change Rate)#

# Short gterm momemtum
df['Mom5'] = df['Close'] / df['Close'].shift(5)
print("Short term : ",df['Mom5'])

# Short term momemtum
df['Mom5'] = df['Close'] / df['Close'].shift(5)
print("Short term : ",df['Mom5'])

# 20-day Price Ratio for monthy mom
df['Mom20'] = df['Close'] / df['Close'].shift(20)
print("Monthly  : ",df['Mom20'])

# Volatility & Liquidity Factors

# For volatilty we caluclate 
# 20-day Rolling Standard Deviation
df['Vol20'] = df['Daily_Return'].rolling(20, min_periods=1).std()
print("Volatility: ",df['Vol20'])

# for liquidity calculate avg vol by the  artio of current vol
df['Volume_Ratio'] = (
    df['Volume'] / df['Volume'].rolling(20, min_periods=1).mean()
)
print("Liquidity: ",df['Volume_Ratio'])

#  High & low range 
df['HL_Range'] = (df['High'] - df['Low']) / df['Close']
print("High and low range: ",df['HL_Range'])

#  today's Open and yesterday's Close 

# diff price gap
df['Gap'] = df['Open'] - df['Close'].shift(1)
print(" Price Gap: ",df['Gap'])

#  Relative Strength Index
# (RSI 14-Day Oscillator)

# diff b/w daily price for mom cal
daily = df['Close'].diff()
print(" Momentum Calculation: ",daily)

# Gain in avg daily price for 14 days
gain = (daily.where(daily > 0, 0)).rolling(14, min_periods=1).mean()
print("Gain in avg daily price: ",gain)

# Loss in avg daily price for 14 days
loss = (-daily.where(daily > 0, 0)).rolling(14, min_periods=1).mean()
print("Loss in avg daily price: ",loss)

# Relative Strength ratio
rs=gain / (loss + 1e-9)
print("Relative Strength ratio: ",rs)

# 14-day Relative Strength Index (RSI)
df['RSI'] = 100 - (100 / (1 + rs))
print("14 days Relative Strength ratio: ",df['RSI'])


#        Moving Average Convergence Divergence (MACD)

# Fast Exponential Moving Average
# calculate 12 Period of ema

ema_12 = df['Close'].ewm(span=12, adjust=False).mean()
print("Fast Exponential Moving Average: ",ema_12)

# Slow Exponential Moving Average
# calculate 26 Period of ema

ema_26 = df['Close'].ewm(span=26, adjust=False).mean()
print("Slow Exponential Moving Average: ",ema_26)

# NOw we will detect (Trend momentum acceleration)
# Diff fast ema - slow

df['MACD'] = ema_12 - ema_26
print("Trend momentum acceleration: ",df['MACD'])

# Bollinger Bands (Price Envelopes)

# Rolling STD of close 20days
df['STD_20'] = df['Close'].rolling(20, min_periods=1).std()
print(" Rolling STD of close 20days: ",df['STD_20'])

# Upper Bollinger Band 
# (MA20 + 2 Standard Deviations)
df['UpperBand'] = df['MA20'] + (df['STD_20'].fillna(0) * 2)
print("Upper Bollinger Band : ",df['UpperBand'])

# Lower Bollinger Band 
# (MA20 - 2 Standard Deviations)
df['LowerBand'] = df['MA20'] - (df['STD_20'].fillna(0) * 2)
print("Lower Bollinger Band : ",df['LowerBand'])

# Dataset Cleanup & Validation

#Fill initial NaN values with zero
dfcleaned = df.fillna(0).copy()

# Print cleaned dataset row and column counts
print(f'\nFeature Engineering Complete! Data Shape: {dfcleaned.shape}')

# SEABORN VISUALIZATIONS & EDA

# Setting Plot canvas size
# Width: 14, Height: 10 inches

plt.figure(figsize=(14, 10))

# Plot 1
# Daily Return Distribution

# 2x2 grid  position
plt.subplot(2, 2, 1)

# Daily returns histogram
# Kernel Density Estimate (KDE) curve plot
sns.histplot(dfcleaned['Daily_Return'], kde=True, color='indigo', bins=50)

# Plot Title
plt.title('Salesforce Daily Return Distribution')

# Plot 2
# Close Price with Bollinger Bands Overlay

# 2x2 grid for 2nd position
plt.subplot(2, 2, 2)

# Plot a historical line chart of close price
plt.plot(
    dfcleaned.index, dfcleaned['Close'], label='Close Price', color='blue', alpha=0.8
)

# Now we wiil plot Upper Bollinger Band plot
# semi-transparent red line
plt.plot(
    dfcleaned.index,
    dfcleaned['UpperBand'],
    label='Upper Band',
    color='red',
    alpha=0.5,
)


# # Now we wiil plot Lower Bollinger Band plot 
# semi-transparent green line
plt.plot(
    dfcleaned.index,
    dfcleaned['LowerBand'],
    label='Lower Band',
    color='green',
    alpha=0.5,
)

# Add title & legened
plt.title('Salesforce (CRM) Price & Bollinger Bands')
plt.legend()

# Plot 3
# Correlation Matrix Heatmap

# 2x2 grid for 3rd position
plt.subplot(2, 2, 3)

# List oof Key quantitative features to check corr
features = [
    'Daily_Return',
    'Vol20',
    'RSI',
    'MACD',
    'Volume_Ratio',
    'HL_Range',
]

# Plotting Heatmap 
sns.heatmap(
    dfcleaned[features].corr(), annot=True, cmap='coolwarm', fmt='.2f'
)

#  For showing numeric correlation values annot=True

# Add title for correlation matrix
plt.title('Feature Correlation Matrix')

# Plot 4
# Relative Strength Index (RSI) Oscillator

plt.plot(dfcleaned.index, dfcleaned['RSI'], color='darkorange', label='RSI 14')
plt.axhline(70, linestyle='--', color='red', alpha=0.7)
plt.axhline(30, linestyle='--', color='green', alpha=0.7)

# Add title for RSI momentum chart
plt.title('RSI Momentum Indicator')

# plot display time
plt.tight_layout()
plt.show()

# Feature Selection & Data Standardization

features_clust = [
    'Daily_Return',
    'Vol20',
    'RSI',
    'MACD',
    'Volume_Ratio',
    'HL_Range',
]

scaler = StandardScaler()

#Fit and transform selected features into zero-mean, unit-variance scale
scaled_features = scaler.fit_transform(dfcleaned[features_clust])

#Dimensionality Reduction (PCA)

# 2 main principal components
pca = PCA(n_components=2)

# Now we willscaled features into 2D components
pca_components = pca.fit_transform(scaled_features)

# Principal Component 1
dfcleaned['PC1'] = pca_components[:, 0]

#  Principal Component 2 
dfcleaned['PC2'] = pca_components[:, 1]

# K-Means Clustering 
# (Market Regimes)

# Initialize KMeans algorithm
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
dfcleaned['Market_Regime'] = kmeans.fit_predict(scaled_features)

# Visualizing Market Regimes

#PCA Market Regime scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(
    x='PC1',
    y='PC2',
    hue='Market_Regime',
    data=dfcleaned,
    palette='Set1',
    alpha=0.7,
)

# chart title and component labels
plt.title('Unsupervised Market Regimes (PCA Space)')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')

plt.legend(title='Market Regime')
plt.show()

print('Unsupervised Clustering Complete!')

#SUPERVISED MACHINE LEARNING MODELING
#Target Variable Creation & Feature Selection
dfcleaned['Target'] = (dfcleaned['Close'].shift(-1) > dfcleaned['Close']).astype(int)

# list for feature col 
colx = [
    'Daily_Return',
    'Vol20',
    'RSI',
    'MACD',
    'Volume_Ratio',
    'HL_Range',
    'Mom5',
    'Mom20',
]
# X and  vector y
X = dfcleaned[colx]
y = dfcleaned['Target']

#Time-Series  Train-Test Split
#(80% Train, 20% Test) 
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, shuffle=False)

#Feature Scaling
scaleml = StandardScaler()
X_train_scaled = scaleml.fit_transform(X_train)
X_test_scaled = scaleml.transform(X_test)

#Model Initialization & Training

# Logistic Regression
model_log = LogisticRegression(random_state=42)

#Random Forest Classifier
model_rain=RandomForestClassifier(n_estimators=100, random_state=42)

#Extra Trees Classifier
model_tree = ExtraTreesClassifier(n_estimators=100, random_state=42)

# Train Logistic Regression classifier on scaled training data
model_log.fit(X_train_scaled, y_train)

# Train Random Forest classifier 
model_rain.fit(X_train_scaled, y_train)

# Train Extra Trees classifier 
model_tree.fit(X_train_scaled, y_train)

# Training 

preds_lr = model_log.predict(X_test_scaled)

# Random Forest
preds_rf = model_rain.predict(X_test_scaled)

#  Extra Trees
preds_et = model_tree.predict(X_test_scaled)

print('\nSupervised Models Trained & Predictions Generated Successfully!')

#MODEL EVALUATION & COMPARISON

def evaluate_model(y_true, y_pred, model_name):
  return {
      'Model': model_name,
      'Accuracy': accuracy_score(y_true, y_pred),
      'Precision': precision_score(y_true, y_pred, zero_division=0),
      'Recall': recall_score(y_true, y_pred, zero_division=0),
      'F1-Score': f1_score(y_true, y_pred, zero_division=0),
  }
  
# Model Performance Aggregation
# Evaluate logistic rain tree

log_metrics = evaluate_model(y_test, preds_lr, 'Logistic Regression')
rain_metrics = evaluate_model(y_test, preds_rf, 'Random Forest')
tree_metrics = evaluate_model(y_test, preds_et, 'Extra Trees')

#all model metrics
result_df = pd.DataFrame([log_metrics, rain_metrics, tree_metrics])
print('\nModel Evaluation Summary:')
print(result_df.round(4).to_string(index=False))

importances = model_rain.feature_importances_
feature_imp = pd.Series(importances, index=colx).sort_values(ascending=False)

#Feature Importance Bar Plot
plt.figure(figsize=(10, 5))
sns.barplot(
    x=feature_imp.values,
    y=feature_imp.index,
    hue=feature_imp.index,
    palette='viridis',
    legend=False,
)

plt.title('Random Forest Feature Importance Analysis')
plt.xlabel('Relative Importance Score')
plt.ylabel('Technical Features')

# Display rendered chart
plt.show()

# backtesting
bt = dfcleaned.loc[X_test.index].copy()
bt['Strat_Return'] = preds_rf[:-1] * bt['Daily_Return'].iloc[1:]

# Calculate cumulative growth for Benchmark and Strategy
bt['Cum_Market'] = (1 + bt['Daily_Return']).cumprod()
bt['Cum_Strat'] = (1 + bt['Strat_Return'].fillna(0)).cumprod()

 # Summary 
 # Print total cumulative returns
print(f"Buy & Hold Return: {bt['Cum_Market'].iloc[-1] - 1:.2%}")
print(f"ML Strategy Return: {bt['Cum_Strat'].iloc[-1] - 1:.2%}")

# Plot cumulative portfolio performance curves
plt.figure(figsize=(10, 5))
plt.plot(bt.index, bt['Cum_Market'], label='Buy & Hold', color='gray', ls='--')
plt.plot(bt.index, bt['Cum_Strat'], label='ML Strategy', color='green', lw=2)
plt.title('Salesforce (CRM) Backtest Results')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# Salesforce (CRM) ML Trading Pipeline - Summary
# Dataset & Scope: Built a 20-year quantitative predictive model using Salesforce daily stock data (2004–2024).
# Feature Engineering:
# Trend & Momentum: Moving Averages (MA20, MA50, MA200), Momentum (Mom5, Mom20).
# Volatility & Oscillators: Vol20, HL_Range, Volume_Ratio, RSI 14, MACD, Bollinger Bands.
# Unsupervised Clustering: Reduced dimensions via PCA and segmented market states into 3 distinct Market Regimes using K-Means.
# Supervised Models: Applied an 80/20 time-series split to train Logistic Regression, Random Forest, and Extra Trees to predict next-day price direction (1 = Up, 0 = Down).
# Key Drivers: Identified Daily_Return, Volume_Ratio, and HL_Range as the top predictive technical features.
# Strategy Backtest: Simulated trading strategy execution against the passive Buy & Hold benchmark to evaluate cumulative returns.