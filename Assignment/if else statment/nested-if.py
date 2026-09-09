# number=int(input("Enter any No"));
# if number>0:
#     print("Number is positive");
#     if number%2==0:
#      print("Number is even");
#     else :
#      print("number is odd")
     
#else: 
   # print("Number is not postive") ;    
   
score = int(input("Enter score"))
attendance = int(input("Enter attendance "))
submitted= input('Submited yes/no ? ');



if score >= 60:
  if attendance >= 80:
    if submitted=='yes':
      print("Pass with good standing")
    else:
      print("Pass but missing assignment")
  else:
    print("Pass but low attendance")
else:
  print("Fail")