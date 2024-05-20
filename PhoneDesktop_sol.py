'''
two integers x and y (0≤x,y≤99) — the number of applications with a 1×1 icon and the number of applications with a 2×2 icon, respectively.

x is for 1x1 block and y is for 2x2 blocks

Logic used : 

In a single screen we have 5x3 = 15 blocks 

For 2x2 icon, maximum of 2 can be accomodated in a single screen, then 7 spaces are left for x
For a single 2x2 icon, 11 spaces are left for 1x1 icons
For 1x1, maximum of 15 can be accomodated in a single screen

First of all we will figure out how many screen are required to fit all the 2x2 icons (e.g y)
Then we will start filling 1x1 icons in the screens occupied by 2x2 icons, once they are done then we will add them in new screen

Code Steps:
1. Check if y is even, (bcoz max of 2 can be accomodated in a single screen)
    if yes then -- initially take no. of screens = y/2
    now the remaining spaces of x = screen*7 (x_place) 
    extra icons left after filling = x_left = x - x_place

    if x_left is multiple of 15 then --> screen = screen + x_left/15
    else :
            screen = screen + x_left/15 + x_left%15

    to make it more efficient, just write
    screen = screen + x_left/15 + x_left%15
    bcoz if it is a multiple of 15 then x_left%15 will be zero


 2. if y is odd
 then screen = y/2 + 1
 x_place = (screen-1)*7 + 11 (occupied_by_2_2x2 + occupied_by_1_1x1)
 then remaining portion is same as above


'''

x,y = 5,2
screen = 0
x_place = 0
x_left = 0

if not (0<=x<=99 and 0<=y<=99):
    print("Limit k bahr mat jaa")

else:
    if not(y%2):
        screen = int(y/2)
        x_place = screen*7
        if x > x_place:
            x_left = x - (x_place)
            screen += int(x_left/15) + x_left%15
    else :
        screen = int(y/2) + 1
        x_place = (screen-1)*7 + 11
        if x > x_place:
            x_left = x - (x_place)
            screen += int(x_left/15) + x_left%15

    print("Required no. of screens are : ",screen)


