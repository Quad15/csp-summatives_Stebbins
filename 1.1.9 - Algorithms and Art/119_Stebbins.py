import turtle as trtl
#name
pizza=trtl
#(for later)pizza.addshape("sauce",(()))

#color of crust
pizza.color("sandybrown")

#size of pizza/painter
pizza.pensize(50)

#draw pizza shape
pizza.fillcolor("gold")
pizza.penup()
pizza.goto(0,-250)
pizza.pendown()
pizza.begin_fill()
pizza.circle(275)
pizza.end_fill()
pizza.penup



'''
#draw crust
pizza.penup()
pizza.goto(0,-225)
pizza.pendown()
pizza.circle(250)
'''

wn = trtl.Screen()
wn.mainloop()