import random
list= ["snake", "water", "gun"]
n=0
win=0
draw=0
loss=0
print("you have 10 rounds for game, lets start")
while n<10:
    your = input("enter your choice")
    comp = random.choice(list)
    if your == "snake":
        if comp == "snake":
            print("draw")
            draw=draw+1
        elif comp == "water":
            print("you won")
            win=win+1
        else:
            print("you loss")
            loss=loss+1
    elif your == "water":
        if comp == "snake":
            print("you loss")
            loss = loss + 1
        elif comp == "gun":
            print("you won")
            win = win + 1
        else:
            print("draw")
            draw = draw + 1
    elif your == "gun":
        if comp == "gun":
            print("draw")
            draw = draw + 1
        elif comp == "water":
            print("you loss")
            loss = loss + 1
        else:
            print("you won")
            win = win + 1
    else:
        print("invalid")
    n=n+1
print("win=",win,"loss=",loss,"draw=",draw)
if win>loss:
    if win> draw:
        print("you won the match")
    else:
        print("draw")
elif loss>win:
    if loss> draw:
        print("you lose the match")
    else:
        print("draw")
else:
    print("your match is draw")

