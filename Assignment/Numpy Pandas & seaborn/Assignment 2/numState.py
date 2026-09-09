import numpy as np

ListYear,DateRecorded,Town,Address,AssessedValue,SaleAmount,=np.genfromtxt('C:/Users/DELL/Documents/AI-Course/my-course-AI-Bin/Plot 2/Real_Estate_Sales_2001-2022_GL-Short.csv',delimiter=',', invalid_raise=False,unpack=True, usecols=(1,2,3,4,5,6),dtype=None,skip_header=1)

print(Address);
print(DateRecorded)
print(Town)
print(ListYear)
print(SaleAmount)
print(AssessedValue) 

# Real State  - statistics operations
SaleAmount = SaleAmount.astype(float)
print(" SaleAmount mean: " , np.mean(SaleAmount))
print("Real State  SaleAmount average: " , np.average(SaleAmount))
print("Real State  SaleAmount std: " , np.std(SaleAmount))
print("Real State  SaleAmount mod: " , np.median(SaleAmount))
print("Real State  SaleAmount percentile - 25: " , np.percentile(SaleAmount,25))
print("Real State  SaleAmount percentile  - 75: " , np.percentile(SaleAmount,75))
print("Real State  SaleAmount percentile  - 3: " , np.percentile(SaleAmount,3))
print("Real State  SaleAmount min : " , np.min(SaleAmount))
print("Real State  SaleAmount max : " , np.max(SaleAmount))

# Real State  SaleAmount  - maths operations
print("Real State  SaleAmount square: " , np.square(SaleAmount))
print("Real State  SaleAmount sqrt: " , np.sqrt(SaleAmount))
print("Real State  SaleAmount pow: " , np.power(SaleAmount,SaleAmount))
print("Real State  SaleAmount abs: " , np.abs(SaleAmount))


# Perform basic arithmetic operations
addition = AssessedValue + SaleAmount
subtraction = AssessedValue - SaleAmount
multiplication = AssessedValue * SaleAmount
division = AssessedValue/SaleAmount

print(" RealState AssessedValue - SaleAmount - Addition:", addition)
print(" RealState AssessedValue - SaleAmount - Subtraction:", subtraction)
print(" RealState AssessedValue - SaleAmount - Multiplication:", multiplication)
print(" RealState AssessedValue - SaleAmount - Division:", division)

#Trigonometric Functions

ValuePie = (AssessedValue/np.pi) +1
# Calculate sine, cosine, and tangent
sine_values = np.sin(ValuePie)
cosine_values = np.cos(ValuePie)
tangent_values = np.tan(ValuePie)

print("Realstate AssessedValue - pie  - Sine values:", sine_values)
print("Realstate AssessedValue - pie Cosine values:", cosine_values)
print("Realstate AssessedValue - pie Tangent values:", tangent_values)

print("Realstate AssessedValue - pie  - Exponential values:", np.exp(ValuePie))


# Calculate the natural logarithm and base-10 logarithm
log_array = np.log(ValuePie)
log10_array = np.log10(ValuePie)

print("Realstate AssessedValue - pie  - Natural logarithm values:", log_array)
print("Realstate AssessedValue - pie  = Base-10 logarithm values:", log10_array)