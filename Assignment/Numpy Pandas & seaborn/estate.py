import pandas as pd
df=pd.read_csv("plots\RealEstate-USA.csv",delimiter=",")
print(df);

print("df - Data types" ,df.dtypes)

print("df.info(): ",df.info)

# display the last three rows
print('Last three Rows:')
print(df.tail(3))

# display the last three rows
print("first thre rows")
print(df.head(3))

#Summary of Statistics of DataFrame using describe() method.
print("Summary of stattics f data frames using describe function ",df.describe);

#Counting the rows and columns in DataFrame using shape(). It returns the no. of rows and columns enclosed in a tuple.
print("Counting of rows and coloums in the data frames unsing shape funtion", df.shape);

# Access the name coloums 
street=df['street']
print("access the name of the coloum: ")
print(street);

#access multiple colums
status_street=df[['status','street']]
print("access multiple columns: df :",status_street)


#Selecting a single row using .loc
second_row=df.loc[1]
print("#Selecting a single row using .loc")
print(second_row)


#Selecting multiple rows using .loc
second_row2 = df.loc[[1, 3]]
print("#Selecting multiple rows using .loc")
print(second_row2)

#Selecting a slice of rows using .loc
df.fillna(0, inplace=True)
second_row3 = df.loc[5:8]
print("#Selecting a slice of rows using .loc")
print(second_row3)
# filling NaN values with 0



#Conditional selection of rows using .loc

second_row4=df.loc[df["street"]=='city']
print("#Conditional selection of rows using .loc")
print(second_row4);


