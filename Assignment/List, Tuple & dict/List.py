#list in Python
""" A build in data type that stores set of values 
 it can store the elements  of diferent datatype ()"""
marks=[87,67,33,95,76];
student=["karan",85,"delhi"];
print("Student Name: " , student[0]);
print("Student Marks: ", marks[0]);
print("City Name: "    , student[2]);
# Like this we can access item
#now accessing items by negative indexing
marks=[87,67,33,95,76];
print(marks[-1]);
#Ranges of indexes 
student_1=[" karan ", 85 , "delhi" , True , "Abdul wahab Awan" , 20 , "Sialkot"];
#like if we want only detail of abdul wahab here we will Range of indexes methods
print(student_1[4:7])
#change of item in list 
#we have a list of student_1 of and i want change the value which is present in 0 index
student_1=[" karan ", 85 , "delhi" , True , "Abdul wahab Awan" , 20 , "Sialkot"];
student_1[0]="Abdul Rehaman";
print(student_1[0]);
# now it will show us Abdul Rehman 
# Change a Range of item Values
student_2=["apple","Banana","cherry","orange","kiwi","mango"];
student_2[1:3]=["Pineapple","watermelon"];
print(student_2);
#Append Items
fruits=["apple","Banana","cherry","orange","kiwi","mango"];
fruits.append("jamun");
fruits[6]="Banana";
fruits[1]="Jamun";
print(fruits);
# here i wanted to add banana to the last of the list and add janum 
# Add Janum at the place of banana.
fruits=["apple","Banana","cherry","orange","kiwi","mango"];
num=[12,23,34,45,65,67];
# here we have two lists named fruits &  num i wanted to add both of them
fruits.append(num);
print(fruits); 

# Clear funtion list 
#Removes all the elements from the list
fruits_1=['apple','banana','cherry','oranges'];
fruits_1.clear();

#copy function list
# Returns a copy of the list
thislist=["apple","Banana","cherry"];
mylist=thislist.copy();
print(mylist);
# count function
#Returns the number of elements with the specified value
num_2=[21,32,43,54,65,67,67,65,343,67];
x=num_2.count(67);
print(x);

#pop function
#Removes the element at the specified position
fruits=["apple","Banana","cherry","orange","kiwi","mango"];
# remove orange
fruits.pop(3);
print(fruits)

fruits=["apple","Banana","cherry","orange","kiwi","mango"];
fruits.reverse();
print(fruits);
#list sort
# we can sort list into two different method Ascending & decending
#Acending List
car=['Audi','lotus','maclerun','covertte',"jeep",'range rover', 'buggati'];
car.sort();
print(car);
# this will order the list in the format of the asceding order. 
#  descending list
num_1=[32,12,34,54,35,46,76,12,98,1,-10,0]
num_1.sort(reverse=True);
print(num_1);