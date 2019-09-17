### SRC - Have you tried running this? the first line looks like it's missing a "

units = int(input("1: Imperial, 2 Metric))  

if units == 1:
    h = float(input("Please Enter the room's height in feet: "))
    w = float(input("Please Enter the room's width in feet: "))
    d= float(input("Please Enter the room's depth in feet: "))
    sq = h * w * 2
    sqa = h * d * 2
    squareft = sq + sqa
    print("You will need ", squareft , " square feet of paint for this room.")

elif units == 2:
    h = float(input("Please Enter the room's height in metres: "))
    w = float(input("Please Enter the room's width in metres: "))
    d= float(input("Please Enter the room's depth in metres: "))
    sq = h * w * 2
    sqa = h * d * 2
    squareft = sq + sqa
    print("You will need ", squareft , " square metres of paint for this room.")

else:
    print("invalid input")

#program assumes room is cuboid



