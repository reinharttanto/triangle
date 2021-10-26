import math
from turtle import *

h = int(input("triangle height:"))
w = int(input("triangle width:"))
z = h / w
angle = (90 - math.degrees(math.atan(z))) + 90
hypo = math.sqrt((h**2) + (w**2))



color('black', 'white')
begin_fill()
right(90)
forward(h)
left(90)
forward(w)
left(angle)
while True:
    forward(1)
    if abs(pos()) <1:
        break

end_fill()
done()
