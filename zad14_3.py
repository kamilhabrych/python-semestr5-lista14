from graphics import *
import time
import random

max_width = 500
max_height = 500

win = GraphWin('Kamil Habrych zadanie 3', max_width, max_height)
win.setBackground('white')

circle = Circle(Point(250,250),50)
circle.setFill('brown')
circle.draw(win)
lengthOfMove = 20
k = ''
moves = ['w','s','a','d']

while True:
    listOfMoves = []
    listOfMoves = moves.copy()
    pt_circle = circle.getCenter()
    r_circle = circle.getRadius()
    if k in listOfMoves: 
        listOfMoves += 5 * [k]
    k = random.choice(listOfMoves)
    if k == 'w' and pt_circle.y-r_circle > 0: 
        circle.move(0,-lengthOfMove)
    elif k == 's' and pt_circle.y+r_circle < max_height: 
        circle.move(0,lengthOfMove)
    elif k == 'a' and pt_circle.x-r_circle > 0: 
        circle.move(-lengthOfMove,0)
    elif k == 'd' and pt_circle.x+r_circle < max_width: 
        circle.move(lengthOfMove,0)
    else: 
        break
    time.sleep(0.1)

win.close() 