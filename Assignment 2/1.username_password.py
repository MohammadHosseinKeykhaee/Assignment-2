username = "Hossein"
password = "hossein.1373"
user = input("Username:")
pas = input("Password:")
if user == username and pas == password:
    print ("Login successful, WELLCOME")
else:
    print ("The username and password are wrong. Please try again")
    c=0
    while c<2:
        user = input("Username:")
        pas = input("Password:")
        print ("The username and password are wrong. Please try again")
        c=c+1
        if c == 2 :
           print("Warning! Account locked")