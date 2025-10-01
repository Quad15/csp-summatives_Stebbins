import turtle as trtl
import random as rand
#name
pizza=trtl
mush=trtl.Turtle(shape='turtle')
mush.color("olive")
pep=trtl.Turtle(shape='circle')
pep.color("firebrick")
#color of crust
pizza.color("sandybrown")
pizza.fillcolor("gold")
#size of pizza/painter
pizza.pensize(50)

#draw pizza shape  
pizza.penup()
pizza.goto(0,-250)
pizza.pendown()
pizza.begin_fill()
pizza.circle(275)
pizza.end_fill()
pizza.penup()

#draw pepperoni
pep_q=trtl.textinput('pep','do you want pepperoni')
if pep_q == 'y': 
    pep_q2=trtl.textinput('pep','how much pepperoni do you want (little bit, normal, alot)')
    if pep_q2 == 'alot':
        for r in range(20):
            randx=rand.randint(-137,137)
            randy=rand.randint(-200,200)
            pep.goto(randx,randy)
            pep.stamp()
    if pep_q2 == 'normal':
        for r in range(10):
            randx=rand.randint(-137,137)
            randy=rand.randint(-200,200)
            pep.goto(randx,randy)
            pep.stamp()
    if pep_q2 == 'little bit':
        for r in range(5):
            randx=rand.randint(-137,137)
            randy=rand.randint(-200,200)
            pep.goto(randx,randy)
            pep.stamp()
mush_q=trtl.textinput('mush','do you want turtles')
if mush_q == 'y': 
    mush_q2=trtl.textinput('pep','how many turtles do you want (little bit, normal, alot)')
    if mush_q2 == 'alot':
        for i in range(20):
            randx=rand.randint(-137,137)
            randy=rand.randint(-200,200)
            mush.goto(randx,randy)
            mush.stamp()
    if mush_q2 == 'normal':
        for i in range(10):
            randx=rand.randint(-137,137)
            randy=rand.randint(-200,200)
            mush.goto(randx,randy)
            mush.stamp()
    if mush_q2 == 'little bit':
        for i in range(5):
            randx=rand.randint(-137,137)
            randy=rand.randint(-200,200)
            mush.goto(randx,randy)
            mush.stamp()
 


'''
#draw crust
pizza.penup()
pizza.goto(0,-225)
pizza.pendown()
pizza.circle(250)
'''

wn = trtl.Screen()
wn.mainloop()