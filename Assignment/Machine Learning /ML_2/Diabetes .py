import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier, GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_auc_score, f1_score

# Set visualization style
sns.set_theme(style="whitegrid")

# 1. Load Dataset
df = pd.read_csv('diabetes_risk.csv')

# 2. Data Preprocessing & Missing Value Handling
df_ml = df.drop(columns=['patient_id']).copy()

# Fill missing categorical values
for col in ['smoking_status', 'alcohol_consumption', 'income_bracket']:
    df_ml[col] = df_ml[col].fillna('Unknown')

# Target Encoding
target_col = 'diabetes_risk'
le_target = LabelEncoder()
df_ml[target_col] = le_target.fit_transform(df_ml[target_col])  # Maps classes to 0, 1, 2

# One-Hot Encoding for Feature Predictors
predictors = [c for c in df_ml.columns if c != target_col]
df_encoded = pd.get_dummies(df_ml[predictors], drop_first=True)

X = df_encoded
y = df_ml[target_col]

# 3. Stratified Train-Test Split (80/20)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Feature Scaling (for Linear Models)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 4. Model Training & Benchmark Evaluation
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000, random_state=42),
    "Gradient Boosting": GradientBoostingClassifier(n_estimators=100, random_state=42),
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
    "Extra Trees": ExtraTreesClassifier(n_estimators=100, random_state=42),
    "Decision Tree": DecisionTreeClassifier(random_state=42)
}

results = []
preds_dict = {}

for name, model in models.items():
    if name == "Logistic Regression":
        model.fit(X_train_scaled, y_train)
        y_pred = model.predict(X_test_scaled)
        y_proba = model.predict_proba(X_test_scaled)
    else:
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        y_proba = model.predict_proba(X_test)
    
    acc = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average='weighted')
    auc = roc_auc_score(y_test, y_proba, multi_class='ovr')
    
    preds_dict[name] = y_pred
    results.append({
        "Model": name, 
        "Accuracy": acc, 
        "F1-Score": f1, 
        "ROC-AUC (OvR)": auc
    })

results_df = pd.DataFrame(results).sort_values(by="Accuracy", ascending=False)
print("\n=== Model Benchmark Results ===")
print(results_df.to_string(index=False))

# 5. Generate Visualizations Figure 1 (Pipeline Overview)
fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# Subplot 1: Target Class Distribution
sns.countplot(x='diabetes_risk', data=df, order=['Low', 'Moderate', 'High'], palette='Set2', ax=axes[0, 0])
axes[0, 0].set_title('1. Diabetes Risk Target Class Distribution', fontsize=12, fontweight='bold')
axes[0, 0].set_xlabel('Diabetes Risk Class')
axes[0, 0].set_ylabel('Patient Count')
for p in axes[0, 0].patches:
    axes[0, 0].annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height() / 2),
                        ha='center', va='center', color='white', fontweight='bold', fontsize=11)

# Subplot 2: Model Benchmark Comparison
results_melted = pd.melt(results_df, id_vars=['Model'], value_vars=['Accuracy', 'F1-Score'], 
                         var_name='Metric', value_name='Score')
sns.barplot(x='Score', y='Model', hue='Metric', data=results_melted, palette='viridis', ax=axes[0, 1])
axes[0, 1].set_title('2. Model Performance Benchmark', fontsize=12, fontweight='bold')
axes[0, 1].set_xlim(0, 1.05)
for p in axes[0, 1].patches:
    width = p.get_width()
    if width > 0:
        axes[0, 1].annotate(f'{width:.3f}', (width + 0.01, p.get_y() + p.get_height() / 2.),
                            ha='left', va='center', fontsize=9)

# Subplot 3: Feature Importances (Random Forest)
rf_model = models["Random Forest"]
importances = pd.Series(rf_model.feature_importances_, index=X.columns).sort_values(ascending=False).head(10)
sns.barplot(x=importances.values, y=importances.index, palette='rocket', ax=axes[1, 0])
axes[1, 0].set_title('3. Top 10 Feature Importances (Random Forest)', fontsize=12, fontweight='bold')
axes[1, 0].set_xlabel('Gini Importance Score')

# Subplot 4: Confusion Matrix (Top Performer)
best_model_name = results_df.iloc[0]['Model']
cm = confusion_matrix(y_test, preds_dict[best_model_name])
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[1, 1],
            xticklabels=le_target.classes_, yticklabels=le_target.classes_)
axes[1, 1].set_title(f'4. Confusion Matrix ({best_model_name})', fontsize=12, fontweight='bold')
axes[1, 1].set_xlabel('Predicted Risk Level')
axes[1, 1].set_ylabel('Actual Risk Level')

plt.tight_layout()
plt.savefig('ml_diabetes_risk_pipeline.png', dpi=300)
plt.show()

# 6. Generate Visualizations Figure 2 (Correlations & Scatter)
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Heatmap
num_cols = ['fasting_blood_sugar', 'hba1c_level', 'age', 'bmi', 
            'waist_circumference_cm', 'blood_pressure_systolic', 
            'blood_pressure_diastolic', 'hours_sleep_per_night', 'stress_level']
corr = df[num_cols].corr()

sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', ax=axes[0], cbar=True)
axes[0].set_title('Clinical & Numerical Features Correlation Matrix', fontsize=12, fontweight='bold')

# Scatter Plot
sns.scatterplot(data=df, x='fasting_blood_sugar', y='hba1c_level', hue='diabetes_risk', 
                hue_order=['Low', 'Moderate', 'High'], palette='Set1', alpha=0.6, ax=axes[1])
axes[1].set_title('Fasting Blood Sugar vs. HbA1c Level by Risk Class', fontsize=12, fontweight='bold')
axes[1].set_xlabel('Fasting Blood Sugar (mg/dL)')
axes[1].set_ylabel('HbA1c Level (%)')

plt.tight_layout()
plt.savefig('feature_correlations_scatter.png', dpi=300)
plt.show()