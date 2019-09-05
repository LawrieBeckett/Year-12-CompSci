from random import randint
p = 1

while p == 1:

    c = str(input("Rock, Paper, Scissors "))

    if c == ("Rock"):
        x = 1
    elif c == ("Scissors"):
        x = 3
    elif c == ("Paper"):
        x = 2

    if c == ("rock"):
        x = 1
    elif c == ("scissors"):
        x = 3
    elif c == ("paper"):
        x = 2


    b = randint(1,3)

    if x == 1 and b == 1:
        print("two rocks: draw")

    elif x == 2 and b == 2:
        print("two papers: draw")

    elif x == 3 and b == 3:
        print("two scissors: draw")

    elif x == 1 and b == 2:
        print("rock and paper: computer wins")

    elif x == 1 and b == 3:
        print("rock and scissors: player wins")

    elif x == 2 and b == 1:
        print("rock and paper: player wins")

    elif x == 2 and b == 3:
        print("scissors and paper: computer wins")

    elif x == 3 and b == 1:
        print("rock and scissors: computer wins")

    elif x == 3 and b == 2:
        print("scissors and paper: player wins")

    p = int(input("keep playing? 1.Yes, 2.No "))
    
