match_number=0
result=0
Lose=0
Draw=0
Win=0
while match_number<8:

    print("Result Game" ,match_number+1, "?? "
    "\nWin : w  Lose : l  Draw : d ")
    G=input()
    if G=="w":
        result+=3
        Win+=1
    elif G=="d":
        result+=1
        Draw+=1
    elif G=="l":
        result+=0
        Lose+=1
    else:
        match_number-=1
        print("Try again")
    match_number+=1
print("Result in 8 matchs is :",Win,"Win",Draw,"Draw", Lose,"Lose"
   "\nFinal ponits : ",result )
