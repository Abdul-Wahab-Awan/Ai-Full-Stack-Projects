import pandas as pd
import numpy as np

data = pd.read_csv('Hunger\FastFoodRestaurants.csv')
# Original data mein se sirf selected columns ko filter karein`
selected_columns = ['address','city','country','keys','latitude','longitude','name','postalCode']
selected_data = data[selected_columns]
# Filtered data ko NumPy array mein convert karein` `numpy_array = selected_data.to_numpy()
selected_data = data[selected_columns]
numpy_array = selected_data.to_numpy()

print(numpy_array);


# Resulting NumPy array ko print karein`


#FAst food csv --- Statics operation 

# Extract longitude and latitude columns as NumPy arrays
# Statistical operations
longitude = data['longitude'].to_numpy()
latitude = data['latitude'].to_numpy()
# Calculate the average longitude value
print("Fast food longitude mean:", np.mean(longitude))
# Calculate the minimum longitude value
print("Fast food longitude min:", np.min(longitude))
# Calculate the maximum longitude value
print("Fast food longitude max:", np.max(longitude))
# Calculate the std longitude value
print("Fast food longitude std:", np.std(longitude))
# Calculate the median longitude value
print("Fast food longitude median:", np.median(longitude))

# Calculate the maximum longitude value
print("Fast food longitude :", np.max(longitude))
# Calculate the 25 per longitude value
print("Fast food longitude max: - 25", np.percentile(longitude,25))
# Calculate the 50 per longitude value
print("Fast food longitude max: - 50", np.percentile(longitude,50))
# Calculate the 75 per longitude value
print("Fast food longitude max: - 75", np.percentile(longitude,50))

longitude = np.nan_to_num(longitude, nan=0)
# fast food  - maths operations
print("longitude square: " , np.square(longitude))
print("longitude sqrt: " , np.sqrt(np.abs(longitude)))
print("longitude Price pow: " , np.power(longitude,2))
print("longitude abs: " , np.abs(longitude))


# Perform basic arithmetic operations
addition = longitude + latitude
subtraction = longitude - latitude
multiplication = longitude * latitude
division = longitude / latitude

print(" FAst Food Long   - lat - Addition:", addition)
print("  FAst Food Long  - lat - Subtraction:", subtraction)
print("  FAst Food Long  Long - lat - Multiplication:", multiplication)
print("  FAst Food Long  Long - lat - Division:", division)

#Trigonometric Functions

longPie = (longitude/np.pi) +1
# Calculate sine, cosine, and tangent
sine_values = np.sin(longPie )
cosine_values = np.cos(longPie )
tangent_values = np.tan( longPie )
 
print("Fast food longitude - div - pie  - Sine values:", sine_values)
print("Fast food longitude - div - pie Cosine values:", cosine_values)
print("Fast food longitude - div - pie Tangent values:", tangent_values)

print("Fast food longitude - div - pie  - Exponential values:", np.exp(longPie))

##this one is creating cause the data this is now handling is in -ve 
# Calculate the natural logarithm and base-10 logarithm
log_array = np.log(np.abs(longPie))
log10_array = np.log10(np.abs(longPie))

print("Fast food longitude- div - pie  - Natural logarithm values:", log_array)
print("Fast food longitude - div - pie  = Base-10 logarithm values:", log10_array)

#Example: Hyperbolic Sine
# Calculate the hyperbolic sine of each element
sinh_values = np.sinh(longPie)
print("Fast food longitude  - div - pie   - Hyperbolic Sine values:", sinh_values)

#Hyperbolic Cosine Using cosh() Function
# Calculate the hyperbolic cosine of each element
cosh_values = np.cosh(longPie)
print("Fast food longitude  - div - pie   - Hyperbolic Cosine values:", cosh_values)

#Example: Hyperbolic Tangent
# Calculate the hyperbolic tangent of each element
tanh_values = np.tanh(longPie)
print("Fast food longitude  - div - pie   -Hyperbolic Tangent values:", tanh_values)

#Example: Inverse Hyperbolic Sine

# Calculate the inverse hyperbolic sine of each element
asinh_values = np.arcsinh(longPie)
print("Fast food longitude  - div - pie   -Inverse Hyperbolic Sine values:", asinh_values)

#Example: Inverse Hyperbolic Cosine
# Calculate the inverse hyperbolic cosine of each element
acosh_values = np.arccosh(longPie)
print("Fast food longitude  - div - pie   -Inverse Hyperbolic Cosine values:", acosh_values)


#Zameen.com Long Plus Lat - 2 dimentional arrary
D2LongLat = np.array([longitude,latitude])

print ("Fast food longitude  Plus Lattitude - 2 dimentional arrary - " ,D2LongLat)

# check the dimension of array1
print("Fast food longitude  Plus Lattitude - 2 dimentional arrary - dimension" , D2LongLat.ndim) 
# Output: 2

# return total number of elements in array1
print("Fast food longitude  Plus Lattitude - 2 dimentional arrary - total number of elements" ,D2LongLat.size)
# Output: 6

# return a tuple that gives size of array in each dimension
print("Fast food longitude  Plus Lattitude - 2 dimentional arrary - gives size of array in each dimension" ,D2LongLat.shape)
# Output: (2,3)

# check the data type of array1
print("Fast food longitude  Plus Lattitude  - 2 dimentional arrary - data type" ,D2LongLat.dtype) 
# Output: int64


