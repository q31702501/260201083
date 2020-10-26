""""
number = float(input("Enter a Number:"))
print("Absolute value: " + str(abs(number)))
"""
number_1=int(input("number 1:"))
number_2=int(input("number 2:"))
number_3=int(input("number 3:"))
if number_1<number_2 and number_1<number_3:
  print(number_1)
elif number_2<number_3 and number_2<number_1:
  print(number_2)
else:
  print(number_3) 
