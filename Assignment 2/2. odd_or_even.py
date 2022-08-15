while 1:
    even= 0
    odd = 0
    number = int(input("please enter a number:"))
    while (number%10)!=0 :
        digits_analyzer =( number%10)
        if (digits_analyzer %2==0) or (digits_analyzer ==0):
          even= even + 1
        else:
          odd = odd + 1
        number= number//10
        print(digits_analyzer, "even digit:", even , digits_analyzer, "odd digit:",odd )
        if(even > odd):
         print("The number of even digits is more")
        else:
         print("The number of odd digits is more")