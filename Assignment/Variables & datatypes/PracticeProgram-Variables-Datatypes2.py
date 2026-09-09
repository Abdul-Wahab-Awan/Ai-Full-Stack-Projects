print("\t\t Same Program But with some different Conditions \t\t")
# we done the last program with all given problems but now it we will make some changes in program
print("\tFirst we will input the value from the user\n\tand atlast we will change the data type of the result ");
#which will go like that 
x=int(input("Enter the first Value: "))#the value user gave to variable we have first told first  
print("Length: ",x)
y=float(input("Enter the Second Value: "))
print("Width: ",y)
area = (x*y); 
print("Area of the Rectangle: ",area);
#here we get the Area mean we got ans now we will change the datatype
# as we seen the ans that is float we can change in integer

area=int(area);
print("Area of the Rectangle: ",int(area))