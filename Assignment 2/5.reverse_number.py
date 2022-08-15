# reverse_number_program
while 1:
  resverse =0
  num_2=num_1=int(input("Please enter a intiger number:"))
  if(num_1>0):
    while(num_1!=0):
     temp=(num_1 % 10)
     resverse =(resverse*10)+temp
     num_1=(num_1//10)
  print(num_2)
  print(resverse)
  print("The Enter number is:",num_2,"and the reverse of the entered number is:", resverse)
  if( resverse == num_2):
       print("Yes, The reversed number is the same as the entered number")
  else:
      print("No, The reversed number is not  the same as the entered number")
  if(num_2<0):
    break
print("Please try again and use only positive and intiger numbers")