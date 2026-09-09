#Step 1
"""Int 1,2,3,4,5,6,7,8,9;
float 1.2, 3.2;
boolean T/F True False
string "Hello World "
If u write
a=7 it will understand by it self that it is integertype
a=7.5 it will understand by it self that it is Floattype"""
a = 7.1  # No semicolon needed here!
print(type(a))
#Step 2
"""We can check our value datatype in your editor while using Python 
like 
when we write 
a=7.1;
print(type(a)) 
it will show our datatype
float 
x=5;
print(x)
print(5*x)
upper code is representing that when we assign a value to a variable 
it get stored it and we can use it now by putting only variable name """
x=5;
print(x)
print(5*x)
"""There is one more thing we can assign more than one variable by 2 differrent method
if we want line by line mean one by one like this
4
5
6 then we do """
a=4
b=5
c=6
print(a);
print(b);
print(c);
# or in efficient way use \n
print("\n",a,"\n",b,"\n",c);
#if we want to print in way quene like 
#1,2,3 not only integer we can add str bool float too.
x,y,z=1,2,"Abdul_Wahab_Awan";
print(x,y,z);
"""we can do simple mathematical operation too, + , - ,* , /, %, 
means Arithematic opertaion"""
a=20;
b=5;
c=a/b; #we can change operation by canging operators here Practice this by *
print(c);
# first we learn about type funtion now we will learn input function
#Input function means that we will ask to user to enter value whatever it will understand it datatype
x=input("Enter your value: ");
print(x);
#We can also check memory addressing in python by using a function which is ID
#like if we enter any value or data in our computer we can check where it is present in our PC RAM.x=5;
y=10;
print(id(x));
print(id(y));
#It will show u different values but when we gave both variable same value it will give u same ID value\
