import turtle as trtl
import random as rand
#name
pizza=trtl
pizza.hideturtle()
mush=trtl.Turtle(shape='turtle')
mush.hideturtle()
mush.color("olive")
pep=trtl.Turtle(shape='circle')
pep.hideturtle()
pep.color("firebrick")
trtl.addshape('pinapple',((25,-13),(25,13),(-12,13),(-12,-15)))
pinapple=trtl.Turtle(shape='pinapple')
pinapple.color('goldenrod')
pinapple.hideturtle()
#color of crust
pizza.color("sandybrown")
pizza.fillcolor("gold")
#size of pizza/painter
pizza.pensize(50)

# list of topping turtles 
toppings = [pep, mush, pinapple]

#draw pizza shape  
pizza.penup()
pizza.goto(0,-250)
pizza.pendown()
pizza.begin_fill()
pizza.circle(275)
pizza.end_fill()
pizza.penup()

#draw pepperoni
pep_q=trtl.textinput('pep','do you want pepperoni (yes/no)')
if pep_q == 'yes': 
    pep_q2=trtl.textinput('pep','how much pepperoni do you want (little bit, normal, alot)')
    if pep_q2 == 'alot':
        for r in range(20):
            randx=rand.randint(-137,137)
            randy=rand.randint(-185,185)
            rand_heading = rand.randint(0,360)
            pep.goto(randx,randy)
            pep.stamp()
    if pep_q2 == 'normal':
        for r in range(10):
            randx=rand.randint(-137,137)
            randy=rand.randint(-185,185)
            rand_heading = rand.randint(0,360)
            pep.goto(randx,randy)
            pep.stamp()
    if pep_q2 == 'little bit':
        for r in range(5):
            randx=rand.randint(-137,137)
            randy=rand.randint(-185,185)
            rand_heading = rand.randint(0,360)
            pep.goto(randx,randy)
            pep.stamp()
mush_q=trtl.textinput('mush','do you want turtles (yes/no)')
if mush_q == 'yes': 
    mush_q2=trtl.textinput('pep','how many turtles do you want (little bit, normal, alot)')
    if mush_q2 == 'alot':
        for i in range(20):
            randx=rand.randint(-137,137)
            randy=rand.randint(-185,185)
            rand_heading = rand.randint(0,360)
            mush.goto(randx,randy)
            mush.stamp()
    if mush_q2 == 'normal':
        for i in range(10):
            randx=rand.randint(-137,137)
            randy=rand.randint(-185,185)
            rand_heading = rand.randint(0,360)
            mush.goto(randx,randy)
            mush.stamp()
    if mush_q2 == 'little bit':
        for i in range(5):
            randx=rand.randint(-137,137)
            randy=rand.randint(-185,185)
            rand_heading = rand.randint(0,360)
            mush.goto(randx,randy)
            mush.stamp()
pinapple_q=trtl.textinput('pinapple','do you want pieapple (yes/no)')
if pinapple_q == 'yes': 
    pinapple_q2=trtl.textinput('pinapple','how much pineapple do you want (little bit, normal, alot)')
    if pinapple_q2 == 'alot':
        for p in range(20):
            randx=rand.randint(-137,137)
            randy=rand.randint(-185,185)
            rand_heading = rand.randint(0,360)
            pinapple.goto(randx,randy)
            pinapple.stamp()
    if pinapple_q2 == 'normal':
        for p in range(10):
            randx=rand.randint(-137,137)
            randy=rand.randint(-185,185)
            rand_heading = rand.randint(0,360)
            pinapple.goto(randx,randy)
            pinapple.stamp()
    if pinapple_q2 == 'little bit':
        for p in range(5):
            randx=rand.randint(-137,137)
            randy=rand.randint(-185,185)
            rand_heading = rand.randint(0,360)
            pinapple.goto(randx,randy)
            pinapple.stamp()
pizza.write("goodbye thank you for eating here.")

'''
#draw crust
pizza.penup()
pizza.goto(0,-225)
pizza.pendown()
pizza.circle(250)
'''

wn = trtl.Screen()
wn.mainloop()