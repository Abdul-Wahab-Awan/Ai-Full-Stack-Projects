#Basic Concept
a="Hello Wahab";
print(a);
#a="Hello";
#b="abc";
#if we want to know that which on greater than or lesser than
# each other then we use those operator mean we do comparison b/w them
""""There is well knowed Ascii Code Table it used to calculate which string value is much greater than
the other it work like this
a=65
b=66 
c=67
mean every single alphabet has its own number it calculate every single alphabet 
by using Asci code table
"""
a="Hello";
b="How are u";
print(a+ "\t",b)
#we can use arithematic operators like that in Strings
print("He"in a); 
#in is operator used for comparison in the strings 
#string Slicing
S="Hello "
"""s=h e l l o
 S[0]=h ,S[1]=e ,S=[2]=l ,S[3]=l, S[4]=[o]"""
# we can pich which we want like if we want h e then we print S[0:1]or (S[0],S[1])
#this help in this way (S[0],S[1]) the value in these indexes will be printed
print(S[0],S[1]);
"""The concept we lerned upabove is above postive number of indexes this consist of a number line so we talk about how negative integers works
for example we done this at above now obeserve indexes that how things work with negative integers
 S[0]=h ,S[1]=e ,S=[2]=l ,S[3]=l, S[4]=[o]
 S[-5]=h ,S[-4]=e ,S=[-3]=l ,S[-2]=l, S[-1]=[o]
   """
print(S[-5],S[-4]);
#There are only two which changed first we as we startcount from right 
"""now the major topic of the string is covered as a fresher but now we will move
toward more topics which important basics"""
#length function used in term for counting that how much char in string
S="aaaaaaaaaaa aaaaaaaaaaa";# suppose we get this strinng
print(len(S));
# same like this we can do much more thing by putting Function in it. 
#like we want to captalize the string
print(S.capitalize());
#like we want to Upper the string
print(S.upper()); 
#like we want to split  the string
S="How are you";
print(S.split(  ));
#like if we have string and we want to fix the string b/w center spaces that contain *
S="Hello";
print(S.center(11,'#')); 
# Note: we cannot remember all the function at the same moment but 
# the most important thing is to know that what to do and how to do



