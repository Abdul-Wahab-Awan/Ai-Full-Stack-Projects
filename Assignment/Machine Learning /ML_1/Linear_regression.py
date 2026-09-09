import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv('Regression/insurance.csv')
print(df.head());
print("df.shape",df.shape)

#So, what's the relationship between these variables? A great way to explore relationships between variables is through Scatter plots. We'll plot the hours on the X-axis and scores on the Y-axis, and for each pair, a marker will be positioned based on their values:
df.plot.scatter(x='age', y='charges', title='Scatter Plot of hours and scores percentages');
plt.show()
df.plot.scatter(x='bmi', y='charges', title='Scatter Plot of bmi and scores percentages');
plt.show()
df.plot.scatter(x='children', y='charges', title='Scatter Plot of children and scores percentages');
plt.show()
df.plot.scatter(x='smoker', y='charges', title='Scatter Plot of children and scores percentages');
plt.show()
df.plot.scatter(x='region', y='charges', title='Scatter Plot of children and scores percentages');
plt.show()
df_num=df[['age','charges']]
print(df_num.corr())

df_num=df[['age','charges']]
print(df_num.describe())

print(" Age:", df['age'])
print(" Age:", df['charges']   )

X=df['age'].values.reshape(-1,1)
Y=df['charges'].values.reshape(-1,1)

print("y:",Y)
print("x:",X)

seed=42;
from sklearn.model_selection import train_test_split

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=seed)


print(X_train) 
print(Y_train)

#Training a Linear Regression Model

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()


#Now, we need to fit the line to our data, we will do that by using the .fit() method along with our X_train and y_train data:

regressor.fit(X_train, Y_train)

print(regressor.intercept_)

print(regressor.coef_)

def calc(slope,intercept,age):
    return slope*age+intercept

score=regressor.predict([[9.5]])
print(score)

y_pred = regressor.predict(X_test)

df_preds=pd.DataFrame({'Actual':Y_test.squeeze(),'Predicted':y_pred.squeeze()})
print(df_preds)

from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
mae=mean_squared_error(Y_test,y_pred)
mse=mean_absolute_error(Y_test,y_pred)
rmse=np.sqrt(mse)
r2=r2_score(Y_test,y_pred)


print(f'Mean absolute error: {mae:.2f}')
print(f'Mean squared error: {mse:.2f}')
print(f'Root mean squared error: {rmse:.2f}')
print(f'R2 Score: {r2:.2f}')


from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

models = {
     "Linear Regression": LinearRegression(),
     "Decision Tree": DecisionTreeRegressor(random_state=seed),
     "Random Forest": RandomForestRegressor(random_state=seed),
     "Support Vector Regression": SVR(),
     "KNN Regressor": KNeighborsRegressor(),
     "Random Regressor": RandomForestRegressor(n_estimators=200, max_depth=10, random_state=seed)
 }

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score ,explained_variance_score

for name, model in models.items():

    # Train
    model.fit(X_train, Y_train.ravel())

    # Prediction
    y_pred = model.predict(X_test)

    # Metrics
    mae = mean_absolute_error(Y_test, y_pred)
    mse = mean_squared_error(Y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(Y_test, y_pred)
    evs=explained_variance_score

    

    print(f"MAE : {mae:.2f}")
    print(f"MSE : {mse:.2f}")
    print(f"RMSE: {rmse:.2f}")
    print(f"R2  : {r2:.2f}")
    
