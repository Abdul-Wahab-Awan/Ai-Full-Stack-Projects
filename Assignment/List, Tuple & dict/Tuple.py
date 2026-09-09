# Tuples are used to store multiple items in a single variable
# A tuple is a collection which is ordered and unchangeable
# tuple are written in round brackets

# Example
mytuple1 = ("apple", "banana", "cherry")

""" In tuple there are few methods
 Access Tuple
 Update Tuple
 Count Tuple
 Index tuple """

# Access tuple
fruits = ("Apple", "banana" , 'cherry')
print(fruits[1])

# Negative indexing 
fruits = ("Apple", "banana" , 'cherry')
print(fruits[-1])

# Ranges of indexes
myfruits = ('Apple','Berries','Carrot','Oranges','kiwi','mango','melon')
print(myfruits[2:5])

# Update Tuple
x = ('apple','banana','cherry')
y = list(x)
y[1] = 'biwi'
x = tuple(y)
print(x)

"""Now there are two main method left 
 Count()
 index()"""

# Count()
# Returns the number of times a specified value occurs in a tuple
mytuple = (1,3,5,7,9,11,5,14,15,17,19,5)
x = mytuple.count(5)
print(x)

#index()
#Searches the tuple for a specified value and returns the position of where it was found
mytuple = (1,3,8,7,9,11,8,14,15,8,19,8);
x = mytuple.count(8)
print(x)

