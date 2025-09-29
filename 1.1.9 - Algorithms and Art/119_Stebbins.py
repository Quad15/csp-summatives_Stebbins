import turtle as trtl

pizza=trtl

#color of crust
pizza.color("wheat")

#size of pizza/painter
pizza.pensize(50)

#draw pizza shape
pizza.fillcolor("tomato")
pizza.penup()
pizza.goto(0,-250)
pizza.pendown()
pizza.begin_fill()
pizza.circle(275)
pizza.end_fill()




'''
#draw crust
pizza.penup()
pizza.goto(0,-225)
pizza.pendown()
pizza.circle(250)
'''

wn = trtl.Screen()
wn.mainloop()