import numpy as np
import pandas as pd
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier  # Added New Model 1
from sklearn.svm import SVC                                                       # Added New Model 2
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from tensorflow.keras.models import Sequential
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout



#Loading DataFrame & Descriptive Statistics

df = pd.read_csv('micro/Microsoft.csv',parse_dates=['Date'], index_col='Date')

# Display summary information including column types and non-null counts
print("Dataset Info:")
df.info()

# Display summary descriptive statistics for numerical columns
print("Descriptive Statistics:")
print(df.describe().T)

# Calculate maximum value for all numerical columns
print("Maximum Operations:")
print(df.select_dtypes(include=[np.number]).max())

print(df.head())
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.describe())
print(df.info())
print(df.isnull().sum())
print(df.duplicated().sum())

print("stat ops ")

print(df[['Open', 'High', 'Low', 'Close', 'Volume']].describe())



# feature engineering

#1. Log Returns & Momentum
# 2. Moving Averages
# 3. Volatility Indicators
# 4. Price & Volume Dynamics
# 5. Technical Indicators
# (RSI, MACD, ATR, BB-Width, %K)


#Log Returns & Momentum

# Log return
df['Log Return'] = np.log(df['Close'] / df['Close'].shift(1))
print(" LOg REturn: ",df['Log Return'])

# 5-day Price  mom
df['Mom5'] = df['Close'] / df['Close'].shift(5)
print("Momentum : ",df['Mom5'])

# 10-day Price  mom
df['Mom10'] = df['Close'] / df['Close'].shift(10)
print("Momentum : ",df['Mom10'])

# 20-day Price  mom
df['Mom20'] = df['Close'] / df['Close'].shift(20)
print("Momentum : ",df['Mom20'])

# Start from MA (Moving Averages)
# Trend Factors

# For calculating the moving average of close price of last 20 day 
df['MA20'] = df['Close'].rolling(20, min_periods=1).mean()
print("Moving Average of Close price last 20 Days ",df['MA20'])

# For calculating the moving average of close price of last 50 day 
df['MA50'] = df['Close'].rolling(50, min_periods=1).mean()
print("Moving Average of Close price last 50 Days ",df['MA50'])

# For calculating the moving average of close price of last 200 day 
df['MA100'] = df['Close'].rolling(100, min_periods=1).mean()
print("Moving Average of Close price last 100 Days ",df['MA100'])

# For calculating the moving average of close price of last 200 day 
df['MA200'] = df['Close'].rolling(200, min_periods=1).mean()
print("Moving Average of Close price last 200 Days ",df['MA200'])

# Volatility Indicators

# For volatilty we caluclate 
# 5-day Rolling Standard Deviation
df['Vol5'] = df['Log Return'].rolling(5, min_periods=1).std()
print("Volatility: ",df['Vol5'])

# 20-day Rolling Standard Deviation
df['Vol10'] = df['Log Return'].rolling(10, min_periods=1).std()
print("Volatility: ",df['Vol10'])

# 20-day Rolling Standard Deviation
df['Vol20'] = df['Log Return'].rolling(20, min_periods=1).std()
print("Volatility: ",df['Vol20'])

# 20-day Rolling Standard Deviation
df['Vol60'] = df['Log Return'].rolling(60, min_periods=1).std()
print("Volatility: ",df['Vol60'])

# calculate HL-Range
df['HL-Range'] = (df['High'] - df['Low']) / df['Close']
print(df['HL-Range'])

#overnight price movement
df['Gap'] = df['Open'] - df['Close'].shift(1)
print("GAp: ",df['Gap'])

#calculate volume ratio
df['Volume Ratio'] = df['Volume'] / df['Volume'].rolling(20).mean()
print(df['Volume Ratio'])

# Calculate RSI

# Calcukatre diff
df['diff'] = df['Close'] - df['Close'].shift(1)
print(df['diff'])

# GAin
df['Gain'] = df['diff'].clip(lower=0)
print(df['Gain'])

# Loss
df['Loss'] = np.absolute(df['diff'].clip(upper=0))
print(df['Loss'])

# avg gain
df['Avg Gain'] = df['Gain'].rolling(14).mean()
print(df['Avg Gain'])

# Avg loss
df['Avg Loss'] = df['Loss'].rolling(14).mean()
print(df['Avg Loss'])

# Rs
df['RS'] = df['Avg Gain'] / df['Avg Loss']
print(df['RS'])

df['RSI'] = 100 - ( 100 / ( 1 + df['RS'] ))
print(df['RSI'])

df.drop(columns=['diff', 'Gain', 'Loss', 'Avg Gain', 'Avg Loss', 'RS'], inplace=True)
print(df['RSI'])

#calculate MACD

# exp 12
df['EMA12'] = df['Close'].ewm(span=12).mean()
print("Ema 12",df['EMA12'])
# exp 26
df['EMA26'] = df['Close'].ewm(span=26).mean()
print("Ema 26",df['EMA26'])

df['MACD'] = df['EMA12'] - df['EMA26']
print("MACD: ",df['MACD'])

# ATR (Average True Range)

t1 = df['High'] - df['Low']
print("ATR 1: ",t1)

t2 = (df['High'] - df['Close'].shift(1)).abs()
print("ATR 2: ",t2)

t3 = (df['Low'] - df['Close'].shift(1)).abs()
print("ATR 3: ",t3)

df['ATR'] = pd.concat([t1, t2, t3], axis=1).max(axis=1).rolling(14).mean()
print("ATR : ",df['ATR'])

# Bollinger Band Width

# standard deviation 20 rolling  of close
std20 = df['Close'].rolling(20).std()
print("standard deviation 20 rolling  of close : ",std20)

# Upper band 
upper = df['MA20'] + (2 * std20)
print("Upper BAnd width : ",std20)

# Lower band 
lower = df['MA20'] - (2 * std20)
print("Lower BAnd width : ",std20)

# bollinger band width
df['BB-Width'] = (upper - lower) / df['MA20']
print("Bollinger Band Width : ",std20)

# Stochastic %K

low14 = df['Low'].rolling(14).min()
print("Stochastic  Low : ",low14)

high14 = df['High'].rolling(14).max()
print("Stochastic High: ", high14)

df['%K'] = ((df['Close'] - low14) / (high14 - low14)) * 100
print("Stochastic %K :",df['%K'] )

# On-Balance Volume (OBV) 
# - Easy Vectorized Logic

price_diff = df['Close'].diff()
print("Price Diff: ",price_diff)

obv_change = np.where(price_diff > 0, df['Volume'], np.where(price_diff < 0, -df['Volume'], 0))
print("On-Balance Volume  : ",obv_change)

df['OBV'] = obv_change.cumsum()
print(df['OBV'])

#Day of week
df['Day of week'] = df.index.dayofweek

# Target Columns
df['Tomorrow Return'] = (df['Close'].shift(-1) / df['Close']) - 1
print("Tomorrow Return: ",df['Tomorrow Return'])

# up/down  of tomorow return
df['Up / Down'] = np.where(df['Tomorrow Return'] > 0, 1, 0)
print(df['Up / Down'])

#  Price Distribution (Histogram + KDE)
# Checking feature skewness
plt.figure(figsize=(8, 4))
sns.histplot(df['Close'], kde=True, color='purple')
plt.title('Stock Closing Price Distribution')
plt.xlabel('Close Price')
plt.ylabel('Frequency')
plt.show()

# SEABORN DATA VISUALIZATION SECTION

#  Outlier Detection (Boxplot)
# Spotting extreme values in Return data
plt.figure(figsize=(8, 3))
sns.boxplot(x=df['Log Return'], color='teal')
plt.title('Outliers Detection in Log Returns')
plt.show()

# Correlation Heatmap
# Checking relationship between technical indicators
plt.figure(figsize=(10, 6))
sns.heatmap(df[['Close', 'MA20', 'MA50', 'RSI', 'MACD', 'ATR']].corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Feature Correlation Heatmap')
plt.show()


# Target Class Balance (Countplot)
# Checking if Up/Down days are balanced
plt.figure(figsize=(6, 4))
sns.countplot(x='Up / Down', data=df, palette='Set2')
plt.title('Target Distribution (0 = Down, 1 = Up)')
plt.show()


# Missing values remove karna
df.dropna(inplace=True)

# MACHINE LEARNING (CLASSIFICATION)
feature_cols = [
    'Log Return', 'Mom5', 'Mom20', 'MA20', 'MA50', 'MA100', 'Vol5', 'Vol10',
    'Vol20', 'Vol60', 'HL-Range', 'Gap', 'Volume Ratio', 'RSI', 'MACD',
    'ATR', 'BB-Width', '%K', 'OBV', 'Day of week'
]

print("List of features: ",feature_cols)

feature_cols = [col for col in feature_cols if col in df.columns]

X = df[feature_cols]
y = df['Up / Down']

# Time Series Split (No Shuffle!)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, shuffle=False)

# Feature Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Model Training
# Logistic Regression

#Logistic Regression classifier
logist_model = LogisticRegression(C=0.1, max_iter=1000)

# Train the model
logist_model.fit(X_train_scaled, y_train)

#Predict target values
y_pred_class = logist_model.predict(X_test_scaled)

#Print model accuracy
print("--- Logistic Regression Results ---")
print("Accuracy:", accuracy_score(y_test, y_pred_class))

# Model 2
# Decision Tree Classifier

tree_model = DecisionTreeClassifier(max_depth=5, random_state=42)

#Train Decision Tree
tree_model.fit(X_train_scaled, y_train)

# Predict target values for test dataset
pred_tree = tree_model.predict(X_test_scaled)

# Print model accuracy score
print(f"2. Decision Tree Accuracy       : {accuracy_score(y_test, pred_tree):.4f}")

#  Model
# Gradient Boosting Classifier
# Initialize Gradient 

gradient = GradientBoostingClassifier(n_estimators=100, learning_rate=0.05, max_depth=3, random_state=42)
# Train Gradient Boosting model on scaled training data
gradient.fit(X_train_scaled, y_train)

# Predict target values for test dataset
pred_gb = gradient.predict(X_test_scaled)

# Print model accuracy score
print(f" Gradient Boosting Accuracy   : {accuracy_score(y_test, pred_gb):.4f}")

# Model 5
# Support Vector Machine (SVC)
# Initialize Support Vector Classifier with RBF kernel
SVM = SVC(kernel='rbf', C=1.0)

# Train SVM classifier on scaled training data
SVM.fit(X_train_scaled, y_train)

# Predict target values for test dataset
pred_svm = SVM.predict(X_test_scaled)

# Print model accuracy score
print(f" Support Vector Machine Accuracy: {accuracy_score(y_test, pred_svm):.4f}")

#DEEP LEARNING (LSTM MODEL)

print("================ DEEP LEARNING (LSTM) ================")

# sliding window length 
# (number of past days used for prediction)
window_size = 30

# Initialize empty lists
X_dl, y_dl = [], []

#30-day historical feature windows

for i in range(window_size, len(df)):
    # Append past 30 days of features
    X_dl.append(df[feature_cols].iloc[i-window_size:i].values)
    
    # Append the target for the current day
    y_dl.append(df['Up / Down'].iloc[i])
    
# Convert sequences to NumPy arrays
X_dl = np.array(X_dl)
y_dl = np.array(y_dl)

# Split data into 
# 80% training and 20% testing

split = int(len(X_dl) * 0.8)
X_train_dl, X_test_dl = X_dl[:split], X_dl[split:]
y_train_dl, y_test_dl = y_dl[:split], y_dl[split:]

# Initialize MinMaxScaler
mm_scaler = MinMaxScaler()

# Reshape 3D array to 2D, scale features
X_train_dl_scaled = mm_scaler.fit_transform(X_train_dl.reshape(-1, X_train_dl.shape[2]))

# Transform test data using the fitted scaler
X_test_dl_scaled = mm_scaler.transform(X_test_dl.reshape(-1, X_test_dl.shape[2]))

# Reshape data back into 3D structure expected by LSTM: [samples, time_steps, features]
X_train_dl_scaled = X_train_dl_scaled.reshape(-1, window_size, len(feature_cols))
X_test_dl_scaled = X_test_dl_scaled.reshape(-1, window_size, len(feature_cols))

# Define Sequential neural network
lstm_model = Sequential([
    # First LSTM layer with 50 units returning output sequences
    LSTM(units=50, return_sequences=True, input_shape=(window_size, len(feature_cols))),
    # Dropout layer to prevent overfitting by deactivating 20% of neurons randomly
    Dropout(0.2),
    # Second LSTM layer with 50 units
    LSTM(units=50),
    # Second Dropout layer
    Dropout(0.2),
    # Output Dense layer with sigmoid activation for binary classification (0 or 1)
    Dense(1, activation='sigmoid')
])

# Compile model using Adam optimizer 
lstm_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the LSTM model
lstm_model.fit(
    X_train_dl_scaled, y_train_dl,
    epochs=15,             # Number of complete passes through training dataset
    batch_size=32,          # Number of samples processed before updating weights
    validation_split=0.1,   # Reserve 10% of training data for validation
    verbose=1               # Suppress output logs during training
)

# Predict output probabilities for test set
lstm_preds_prob = lstm_model.predict(X_test_dl_scaled)
# Convert probabilities to binary predictions (1 if probability >= 0.5, else 0)
lstm_preds = (lstm_preds_prob >= 0.5).astype(int).ravel()
# Print LSTM accuracy score
print(f"6. LSTM Deep Learning Accuracy : {accuracy_score(y_test_dl, lstm_preds):.4f}")

# Extract test set
backtest_df = df.iloc[-len(X_test):].copy()
backtest_df['Prediction'] = pred_gb

# Calculate daily strategy returns
backtest_df['Strategy Return'] = np.where(backtest_df['Prediction'] == 1, backtest_df['Tomorrow Return'], 0)
print("aily strategy returns: ",backtest_df['Strategy Return'])

# Calculate cumulative growth
backtest_df['Cumulative Strategy'] = (1 + backtest_df['Strategy Return']).cumprod()
print("Cumulative Strategy:",backtest_df['Cumulative Strategy'])

#Buy & Hold strategy
backtest_df['Cumulative Buy & Hold'] = (1 + backtest_df['Tomorrow Return']).cumprod()
print("Buy and Hold:",backtest_df['Cumulative Buy & Hold'])




# Print final cumulative return multipliers
print(f"Final Strategy Multiple  : {backtest_df['Cumulative Strategy'].iloc[-1]:.2f}x")
print(f"Final Buy & Hold Multiple: {backtest_df['Cumulative Buy & Hold'].iloc[-1]:.2f}x")

# Initialize plot figure with custom size
plt.figure(figsize=(10, 5))

# Plot cumulative strategy returns line
plt.plot(backtest_df['Cumulative Strategy'], label='GBM Strategy Return', color='green')

# Plot cumulative benchmark buy & hold returns line
plt.plot(backtest_df['Cumulative Buy & Hold'], label='Buy & Hold Return', color='orange')

# Set chart title
plt.title('Backtesting Performance - Gradient Boosting vs Benchmark')

# Set Y-axis label
plt.ylabel('Cumulative Growth')

# Display legend box
plt.legend()

plt.show()


# 1. Microsoft Stock Prediction & Algorithmic Trading Pipeline
# 1. Data Processing & Feature Engineering

# Market Indicators: Transformed raw stock data to construct advanced technical indicators (RSI, MACD, Bollinger Bands, ATR, and OBV).

# Volatility & Momentum: Calculated moving averages from 5 to 200 days, along with volatility and momentum features, allowing the model to capture deep market trends.

# 2. Exploratory Data Analysis (EDA)

# Visual Insights: Generated closing price distributions, log return outlier plots, and feature correlation heatmaps using Seaborn.

# Target Balance: Verified the balance between "Up" and "Down" stock movement days, ensuring a well-conditioned dataset for classification models.

# 3. Machine Learning Classification

# Traditional Models: Normalized features using StandardScaler and trained robust classifiers (Logistic Regression, Decision Tree, Gradient Boosting, and SVM).

# Predictive Power: Predicted the next day's stock direction (0 = Down, 1 = Up) based on historical market data.

# 4. Deep Learning (LSTM Time-Series)

# Sequential Learning: Reshaped data into a 3D format using a 30-day sliding window and MinMaxScaler.

# Neural Network: Trained a 2-layer Long Short-Term Memory (LSTM) network with Dropout layers to capture complex sequence patterns and future trends from the prior 30 days.

# 5. Strategy Backtesting & Evaluation

# Algorithmic Trading: Simulated an algorithmic trading strategy using predictions from the Gradient Boosting model (Predict 1 = Buy, 0 = Hold).

# Performance Benchmark: Plotted the cumulative returns of the ML strategy against the traditional "Buy & Hold" approach to evaluate real-world profitability multiples.