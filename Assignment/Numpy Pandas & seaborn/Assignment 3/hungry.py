import pandas as pd
df=pd.read_csv('Hunger\FastFoodRestaurants.csv',delimiter=",");
print(df);



print("df - data types" , df.dtypes)

print("df.info():   " , df.info() )

# display the last three rows
print('Last three Rows:')
print(df.tail(3))

# display the first three rows
print('First Three Rows:')
print(df.head(3))
print()

#Summary of Statistics of DataFrame using describe() method.
print("Summary of Statistics of DataFrame using describe() method", df.describe())

#Counting the rows and columns in DataFrame using shape(). It returns the no. of rows and columns enclosed in a tuple.
print("Counting the rows and columns in DataFrame using shape() : " ,df.shape)
print()

# access the Name column
Countrycol = df['country']
print("access the Name column: df : ")
print(Countrycol);
print()

# access multiple columns
Countrycolcity = df[['country','city']]
print("access multiple columns: df : ")
print(Countrycolcity)
print()

#Selecting a single row using .loc
second_row = df.loc[1]
print("#Selecting a single row using .loc")
print(second_row)
print()

#Selecting multiple rows using .loc
second_row2 = df.loc[[1, 3]]
print("#Selecting multiple rows using .loc")
print(second_row2)
print()

#Selecting a slice of rows using .loc
second_row3 = df.loc[1:5]
print("#Selecting a slice of rows using .loc")
print(second_row3)
print()

#Conditional selection of rows using .loc
second_row4 = df.loc[df['city'] == 'Saluda']
print("#Conditional selection of rows using .loc")
print(second_row4)
print()


#Selecting a single column using .loc
second_row5 = df.loc[:1,'city']
print("#Selecting a single column using .loc")
print(second_row5)
print()


#Selecting multiple columns using .loc
second_row6 = df.loc[:1,['city','country']]
print("#Selecting multiple columns using .loc")
print(second_row6)
print()

#Selecting a slice of columns using .loc
second_row7 = df.loc[:1,'longitude':'lattitude']
print("#Selecting a slice of columns using .loc")
print(second_row7)
print()

#Combined row and column selection using .loc
second_row8 = df.loc[df['city'] == 'Gateway Properties','location':'agency']
print("#Combined row and column selection using .loc")
print(second_row8)
print()

# Case 1 : using .loc - default case - ends here

print("# Case 2 : using .loc with index_col - starts here")
# Case 2 : using .loc with index_col - starts here
# Second cycle - with index_col as property_id
# Why Second cycle - Note Index - , index_col='property_id'


df_index_col = pd.read_csv('Hunger\FastFoodRestaurants.csv',delimiter=",", index_col='keys')

print(df_index_col)
print(df_index_col.dtypes)
print(df_index_col.info())


print(df_index_col)
print(df_index_col.dtypes)
print(df_index_col.info())
# Second cycle - with index_col as  keys

#Selecting a single row using .loc
second_row9= df_index_col.loc['us/oh/hamilton/4182tonyatrl/-1055723171']
print("#Selecting a single row using .loc")
print(second_row9)
print()


#Selecting multiple rows using .loc
second_row10 = df_index_col.loc[['us/oh/englewood/590smainst/-1055723171', 'us/ok/oklahomacity/1535nw50thst/-1161002137']]
print("#Selecting multiple rows using .loc")
print(second_row2)
print()


#Selecting a slice of rows using .loc
second_row11 = df_index_col.loc['us/nd/minot/140024thavesw/-1161002137':'us/ok/shawnee/450nharrisonave/1780593795']
print("#Selecting a slice of rows using .loc")
print(second_row11)
print()

#Selecting a single column using .loc
second_row12= df_index_col.loc[:'us/ny/auburn/225grantave/-2061630068','longitude']
print("#Selecting a single column using .loc")
print(second_row12)
print()

#Selecting multiple columns using .loc
second_row13 = df_index_col.loc[:'us/ny/auburn/225grantave/-2061630068',['city','country']]
print("#Selecting multiple columns using .loc")
print(second_row13)
print()

#Selecting a slice of columns using .loc
second_row14= df_index_col.loc[:'us/ks/lawrence/4651w6thst/-66712705','city':'country']
print("#Selecting a slice of columns using .loc")
print(second_row14)
print()


#Combined row and column selection using .loc
second_row15 = df_index_col.loc[df_index_col['city'] == 'Tell City','address':'country']
print("#Combined row and column selection using .loc")
print(second_row15)
print()


# Case 2 : using .loc with index_col  -  ends here


print("# Case 3 : Using .iloc - starts here")
# Case 3 : Using .iloc - starts here
"""Using .iloc: Selection by Integer Position
.iloc selects by position instead of label. This is the standard syntax of using .iloc: df.iloc[row_indexer, column_indexer]. There are two special things to look out for:

Counting starting at 0: The first row and column have the index 0, the second one index 1, etc.
Exclusivity of range end value: When using a slice, the row or column specified behind the colon is not included in the selection."""


#Selecting a single row using .iloc
second_row16 = df_index_col.iloc[0]
print("#Selecting a single row using .iloc")
print(second_row16)
print()

#Selecting multiple rows using .iloc
second_row17 = df_index_col.iloc[[1, 3,5]]
print("#Selecting multiple rows using .iloc")
print(second_row17)
print()

#Selecting a slice of rows using .iloc
second_row18 = df_index_col.iloc[2:5]
print("#Selecting a slice of rows using .iloc")
print(second_row18)
print()

#Selecting a single column using .iloc
second_row19 = df_index_col.iloc[:,2]
print("#Selecting a single column using .iloc")
print(second_row19)

#Selecting multiple columns using .iloc
second_row20 = df_index_col.iloc[:,[2,4]]
print("#Selecting multiple columns using .iloc")
print(second_row20)
print()




#Selecting a slice of columns using .iloc
second_row21 = df_index_col.iloc[:,2:4]
print("#Selecting a slice of columns using .iloc")
print(second_row21)
print()

#Combined row and column selection using .iloc
second_row22 = df_index_col.iloc[[1, 3,5],2:4]
print("#Combined row and column selection using .iloc")
print(second_row22)
print()

# Case 3 : Using .iloc - ends here

# Next Run 
print("Next Run")

""""Pandas DataFrame Manipulation
DataFrame manipulation in Pandas involves editing and modifying existing DataFrames. Some common DataFrame manipulation operations are:

Adding rows/columns
Removing rows/columns
Renaming rows/columns"""

 # Remove  Rows/ Coloums from a pandas dataframe

 #del row with index 1
df.drop(1,axis=0,inplace=True)

# # del row with index 1 
df.drop(index=2,inplace=True)

# # delete rows with index 3 and 5

df.drop([3,5],axis=0, inplace=True)

# # display the modified df after deleting Rows
print("Modified DataFrame - Remove Rows:")
print(df);












# # delete age columm