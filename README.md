# ⚡ Production-Grade AI & Quantitative Finance Pipeline

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange.svg)](https://www.tensorflow.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.x-F7931E.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An end-to-end framework for financial time-series forecasting, quantitative market regime analysis, and algorithmic trading simulation. This repository houses production-ready machine learning and deep learning pipelines optimized for headless terminal execution, thread safety, and multi-asset backtesting.

---

## 📐 System Architecture
[ Raw Market Data ]
                                       │
                                       ▼
                 ┌───────────────────────────────────────────┐
                 │ Data Preprocessing & Hygiene Layer         │
                 │ - Chronological Sorting & Deduplication   │
                 │ - Missing Value Imputation (Zero-Open Fix)│
                 └─────────────────────┬─────────────────────┘
                                       │
                                       ▼
                 ┌───────────────────────────────────────────┐
                 │ Feature Engineering & Risk Engine         │
                 │ - Volatility (Vol5 to Vol60)              │
                 │ - Momentum & Trends (MA5 to MA200)        │
                 │ - Oscillators & Volume (RSI, MACD, OBV)   │
                 └─────────────────────┬─────────────────────┘
                                       │
                    ┌──────────────────┴──────────────────┐
                    ▼                                     ▼
  ┌───────────────────────────────────┐ ┌───────────────────────────────────┐
  │ Statistical Testing & Regime Analytics│ │ Supervised Learning & Sequence ML │
  │ - ADF Test (Stationarity Check)   │ │ - Scaled Feature Split (80/20)    │
  │ - PCA Decomposition (PC1 / PC2)   │ │ - Classifiers (GBM, RF, SVM, LR)  │
  │ - Isolation Forest (Anomalies)    │ │ - 3D Sequence LSTM Model          │
  └─────────────────┬─────────────────┘ └─────────────────┬─────────────────┘
                    │                                     │
                    └──────────────────┬──────────────────┘
                                       │
                                       ▼
                 ┌───────────────────────────────────────────┐
                 │ Execution Engine & Backtesting Module     │
                 │ - Non-Interactive Headless Rendering      │
                 │ - Signal Simulation vs. Buy & Hold        │
                 │ - Risk-Adjusted Cumulative Metrics        │
                 └───────────────────────────────────────────┘

---

## 🔑 Key Engineering Innovations & Solutions

### 1. Terminal Freeze & Thread Deadlock Mitigation
* **Problem:** Conflict between OpenMP/BLAS backends, TensorFlow, and Matplotlib's interactive GUI event loop caused process hangs during VS Code debugger sessions.
* **Solution:** Configured non-interactive headless rendering via `matplotlib.use('Agg')` and explicit single-threading environment variables (`OMP_NUM_THREADS=1`, `OPENBLAS_NUM_THREADS=1`) to guarantee fast, deterministic script completion.

### 2. Temporal Data Leakage Elimination
* **Problem:** Naive shuffling or improper rolling window sequencing introduces forward look-ahead bias into financial predictors.
* **Solution:** Strictly enforced chronological time-series splitting (80/20 train/test ratio without shuffling) and standard feature scaling fit strictly on historical training frames.

### 3. Quantitative Risk & Market Regime Discovery
* **Dimensionality Reduction:** Compressed 8 core technical indicators via Principal Component Analysis (PCA) to decouple trend magnitude from short-term momentum.
* **Anomaly Detection:** Deployed an `Isolation Forest` (contamination = 0.01) to dynamically flag tail-risk anomalies and price shock spikes.

---

## 📊 Modules & Benchmark Performance

### Module 1: Microsoft Stock Machine Learning & LSTM Pipeline
* **Objective:** Short-term directional movement classification ($0 = \text{Down}, 1 = \text{Up}$) with robust multi-threaded execution.
* **Feature Set:** Log Returns, $Mom_5$, $Mom_{20}$, $MA_{20}$ through $MA_{200}$, $Vol_5$ to $Vol_{60}$, RSI, MACD, ATR, BB-Width, OBV, and Temporal Day-of-Week encodings.
* **Deep Learning Engine:** 2-Layer LSTM with 50 hidden units each, dropout regularization ($0.2$), and a 30-day sliding sequence window.

### Module 2: Adobe Historical Analysis & Algorithmic Backtesting
* **Dataset Horizon:** 9,453 trading sessions (1986 – 2024)[cite: 2].
* **Statistical Rigor:** Verified return stationarity using the Augmented Dickey-Fuller (ADF) test and non-normality via D'Agostino-Pearson testing[cite: 2].
* **Backtest Strategy Results:**

| Strategy / Model | Accuracy | Strategy Cumulative Return | Benchmark (Buy & Hold) | Net Outperformance |
| :--- | :---: | :---: | :---: | :---: |
| **Random Forest Classifier** | **53.15%**[cite: 2] | **Outperformed Benchmark**[cite: 2] | Baseline | **+16.55%**[cite: 2] |
| **LSTM Deep Learning** | **52.88%**[cite: 2] | -- | -- | -- |
| **Logistic Regression** | Baseline[cite: 2] | -- | -- | -- |

> **Key Result:** The Random Forest algorithmic strategy generated a **+16.55% net outperformance** over the baseline Buy & Hold strategy while significantly reducing maximum drawdown exposures[cite: 2].

---

## 💻 Tech Stack & Dependencies

```text
Core Languages:     Python 3.10+
Data Engineering:   Pandas, NumPy
Statistical Inference: SciPy, Statsmodels
Machine Learning:   Scikit-Learn (Ensembles, PCA, IsolationForest, Linear Models)
Deep Learning:      TensorFlow, Keras (Recurrent Neural Networks / LSTM)
Visualization:      Matplotlib (Agg Backend), Seaborn

git clone [https://github.com/Abdul-Wahab-Awan/Ai-Full-Stack-Projects.git](https://github.com/Abdul-Wahab-Awan/Ai-Full-Stack-Projects.git)
cd Ai-Full-Stack-Projects

# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate

pip install numpy pandas matplotlib seaborn scipy statsmodels scikit-learn tensorflow


# Execute Microsoft Pipeline
python micro/mricro.py

# Execute Adobe Pipeline
python adobe/Project1Adobe.py

Abdul Wahab Awan

GitHub: @Abdul-Wahab-Awan

⭐ Star this repository if you find it useful for financial engineering and Quantitative AI development!

This version showcases your technical decision-making, debugging skills, and quantitative finance expertise to any developer or hiring team reviewing your portfolio!
