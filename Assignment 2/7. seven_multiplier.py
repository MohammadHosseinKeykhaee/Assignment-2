number=int(input("please enter the number : "))
if(number%7==0):
    print("Yes, This number is a multiple of 7")
else:
   next_number=(7-(number%7))+number
print(next_number, "is the next multiple of 7.")