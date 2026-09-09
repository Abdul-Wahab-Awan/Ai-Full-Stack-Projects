"""There are two types of functons
 1 build in Functions 
i.e 
input() Calling
print()
len()
"""
# User Defined Function
# Arithematic Calculator

def sum(a,b):
    ans=a+b
    print(ans)
def mul(a,b):
   ans=a*b
   print(ans)
def div(a,b):
    ans=a/b
    print(ans)
def sub(a,b):
    ans=a-b
    print(ans)
    
a=float(input("Enter Any Value:"))
print(a)
b=float(input("Enter any Value:"))
print(b)

sum(a,b)
mul(a,b)
div(a,b)
sub(a,b)