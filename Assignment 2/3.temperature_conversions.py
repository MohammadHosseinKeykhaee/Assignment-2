# Temc : 
while 1:
    temp_1 = input("select your first scale: C or K or F ?: ")
    temp_2 = input("select your second scale: C or K or F ?: ")
    temperature = float(input("please enter a temperature according to the first unit: "))
    if (temp_1 == "C" or temp_1 =="c" or temp_1 =="Celsius" or temp_1 == "K" or temp_1 =="k"  or temp_1 =="kelvin" or  temp_1 == "F" or temp_1 == "f"  or temp_1 =="Fahrenheit") and (temp_2 == "C" or temp_2 ==  "c" or temp_2 == "Celsius" or temp_2 == "K" or temp_2 == "k"  or  temp_2 == "kelvin" or temp_2 == "F" or  temp_2 == "f"  or temp_2 == "Fahrenheit"):
        if(temp_1 == "C" or temp_1 =="c" or temp_1 =="Celsius" and temp_2 == "K" or temp_2 == "k"  or  temp_2 == "kelvin"):
            convertor_temperature =  temperature + 273.15
        elif(temp_1 == "K" or temp_1 == "k"  or  temp_1 == "kelvin" and temp_2 == "C" or temp_2 =="c" or temp_2 =="Celsius" ):
            convertor_temperature =  temperature - 273.15
        elif(temp_1 == "K" or temp_1 == "k"  or  temp_1 == "kelvin" and temp_2 == "F" or temp_2 =="f" or temp_2 =="Fahrenheit"):
            convertor_temperature =  (1.8 * (temperature-273)) + 32
        elif(temp_1 == "F" or temp_1 =="f" or temp_1 =="Fahrenheit" and temp_2 == "K" or temp_2 == "k"  or  temp_2 == "kelvin"):
            convertor_temperature = (temperature + 459.67) / 1.8
        elif(temp_1 == "C" or temp_1 =="c" or temp_1 =="Celsius" and temp_2 == "F" or temp_2 =="f" or temp_2 =="Fahrenheit"):
            convertor_temperature = (temperature * 1.8) +32
        elif(temp_1 == "F" or temp_1 =="f" or temp_1 =="Fahrenheit" and temp_2 == "C" or temp_2 =="c" or temp_2 =="Celsius"):
            convertor_temperature = (temperature - 32) / 1.8
        print(temperature, temp_1, "is",  convertor_temperature, temp_2 )
    else:
        print("!!!!A mistake has occurred!!!!....Try again")