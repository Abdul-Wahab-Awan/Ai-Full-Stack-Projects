"""The elif keyword is Python's way of saying "i
f the previous conditions were not true, then try this condition
"""
a=24;
b=42;
if b>a:
    print("b is greater than a");

elif a>b:
   print("a is greater than b");

elif a==b:
    print("Both a and b are equal ");
 

 # the most usely funtionality of the Elif statement that we can process one
 # entity multiple times

marks=int(input("Enter the score: "));
print('Your obtained Marks:', marks);
if marks>=90:
   print("Grade A")
elif  marks>=80:
   print("Grade B")
elif  marks>=70:
   print("Grade C")
elif  marks>=60:
   print("Grade D");
elif  marks>=50:
   print("Grade D-")
elif  marks<=50:
   print("Grade F");