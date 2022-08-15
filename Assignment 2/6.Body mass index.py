#Body mass index
while (1):
   weight=float(input("Please enter your weight (kilograms):"))
   height=float(input("Please enter your height (meters):"))
   BMI= (weight/(height**2))
   if(15<BMI<50):
     if(BMI<16):
       result=("Result:!Warning! You are very thin and malnourished. Please resort to a nutritionist as soon as possible")
     elif(16<=BMI<=18.5):
        result=(" Result:weight deficit....You are a little thin, and you can achieve optimal conditions with proper diet and nutrition")
     elif(18.51<BMI<24.99):
         result=("Result: Normal,Well done. Your condition is very good and favorable")
     elif(25<BMI<29.99):
         result=("Result:overweight,  You are slightly overweight and on the verge of obesity, and you should exercise more and take care of your nutritional status")
     elif(30<BMI<34.99):
         result=("Result: obesity first degree. You are fat, and if you continue with your improper diet, you may suffer from cardiovascular diseases. Please exercise regularly.")
     elif(35<BMI<=40):
          result=("Result: obesity second degree. You are very obese and you should start your diet with the advice of your doctor. Please exercise regularly.")
     elif(BMI>40):
          result=("Result: obesity third degree, !warning! ... You suffer from obesity. Please resort to a doctor immediately")
          print("Your Body mass index is",BMI)
          print("Advice:",result)
   else:
    print("Error!!! Please Try again!!! and enter your height (m) and weight(kg) correctly ")