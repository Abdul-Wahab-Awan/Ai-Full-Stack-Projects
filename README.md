# 🚀 AI & Full-Stack Data Science Projects

Welcome to the **AI & Full-Stack Data Science Projects** repository! This repository contains end-to-end Machine Learning, Deep Learning, Quantitative Finance, and Full-Stack AI implementations. Each project covers everything from data hygiene and technical feature engineering to predictive modeling, algorithmic strategy backtesting, and production-ready script stabilization.

---

## 📌 Repository Overview

This repository showcases advanced data analytics and algorithmic modeling pipelines built for high-performance financial market forecasting and full-stack integration.

### Key Highlights
* **Comprehensive Data Hygiene:** Handling missing values, corporate actions, invalid pricing, and chronological sorting across decades of market data.
* **Financial Feature Engineering:** Custom technical indicators including RSI, MACD, Bollinger Bands, ATR, OBV, and multi-period Moving Averages ($MA_5$ to $MA_{200}$).
* **Advanced Exploratory Data Analysis:** Market regime identification using Principal Component Analysis (PCA), normality/stationarity testing (ADF, D'Agostino-Pearson), and outlier/anomaly detection via Isolation Forests.
* **Machine Learning & Deep Learning:** Multi-model classification frameworks featuring Logistic Regression, Decision Trees, Random Forests, Gradient Boosting, SVMs, and 3D time-series LSTM Neural Networks.
* **Algorithmic Strategy Backtesting:** Simulating real-world trading strategies (Signal Execution vs. Buy & Hold Benchmarks) to measure cumulative growth multiples and drawdown reduction.

---

## 🛠️ Featured Projects

### 1. Microsoft Stock Direction Prediction & Algorithmic Trading Pipeline
An end-to-end machine learning pipeline built to predict short-term stock movements and backtest algorithmic trading execution without terminal thread-locking or debugging freezes.

* **Data & Features:** Processed historical daily records with engineered log returns, rolling volatility, momentum metrics, and technical indicators (RSI, MACD, ATR, BB-Width, OBV).
* **Modeling:** Evaluated Logistic Regression, Decision Trees, Gradient Boosting, SVMs, and a 30-day sliding window LSTM network.
* **Execution & Backtesting:** Implemented non-interactive headless rendering (`Agg` backend) and thread-safe execution to simulate Gradient Boosting signal performance against traditional Buy & Hold benchmarks.

---

### 2. Adobe (ADBE) Long-Term Stock Analysis & ML Trading Pipeline
A complete historical financial analysis (1986 – 2024) analyzing over 9,400+ trading rows to uncover market regimes and build predictive execution models.

* **Data Hygiene & Preprocessing:** Resolved legacy dataset errors (e.g., zero-valued open prices from 1986–1987) and built chronological time-series pipelines.
* **Statistical Insights & PCA:** Reduced 8 technical features down to 2 principal components (PC1/PC2) to visualize bull/bear market regimes and flagged extreme market shocks using Isolation Forests.
* **Machine Learning & Backtesting:** Trained classifiers on an un-shuffled 80/20 time-series split. The **Random Forest Classifier** achieved the top classical performance (~53.15% accuracy), outperforming the "Buy & Hold" benchmark by **+16.55%** in backtests while significantly mitigating drawdown risk.

---

## 🧰 Tech Stack & Tools

* **Languages:** Python 3.10+
* **Data Manipulation & Stats:** Pandas, NumPy, SciPy, Statsmodels
* **Machine Learning:** Scikit-Learn (Classifiers, StandardScaler, MinMaxScaler, PCA, IsolationForest)
* **Deep Learning:** TensorFlow / Keras (LSTM, Sequential API, Dropout)
* **Data Visualization:** Matplotlib, Seaborn
* **Environment:** VS Code, Git / GitHub

---

## ⚙️ Setup & Installation

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/Abdul-Wahab-Awan/Ai-Full-Stack-Projects.git](https://github.com/Abdul-Wahab-Awan/Ai-Full-Stack-Projects.git)
   cd Ai-Full-Stack-Projects

   pip install numpy pandas matplotlib seaborn scipy statsmodels scikit-learn tensorflow

   # Run the Microsoft Financial Pipeline
python mricro.py

# Run the Adobe Historical Stock Pipeline
python Project1Adobe.py


Would you like me to tailor any specific section further, such as adding a dedicated section for upcoming project roadmaps or API deployment steps?
