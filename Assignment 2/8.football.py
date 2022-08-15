#football
match_number=0
Lose=0
Draw=0
Win=0
result=0
while match_number<8:
    print("GAME" ,match_number+1, "Please input Result Game: ""\nwin : w  lose : l  draw : d ")
    G=input()
    if G=="W" or "w":
        result=result + 3
        Win= Win +1
    elif G=="D" or "d":
        result=result + 1
        Draw=Draw+1
    elif G=="L" or "l":
        result=result + 0
        Lose=Lose+ 1
    else:
        match_number=match_number-1
        print("Try again")
    match_number+=1
print("Result in 8 matchs : ",Win,"win",Draw,"draw", Lose,"lose" "\nFinal points : ",result )