import turtle as trtl 
import random as rand
import leaderboard as lb
wn = trtl.Screen()
#-----game configuration----

leaderboard_file_name = "125_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
max_chars = 6
player_name =trtl.textinput('name','enter your name with max chars'+str(max_chars)+':')
leader_names_list = lb.get_names('125_leaderboard.txt')
leader_scores_list = lb.get_scores('125_leaderboard.txt')
player_name = player_name[:max_chars]

wn.register_shape("poacher1.gif") 
wn.register_shape("poacher2.gif") 
wn.register_shape("poacher3.gif")
wn.register_shape("poacher4.gif")
wn.register_shape("hippo.gif") 

poacher11="poacher1.gif"
poacher22 = "poacher2.gif"
poacher33 = "poacher3.gif"
poacher44 = "poacher4.gif"
hippo1 = "hippo.gif"

poacher1 = trtl.Turtle(shape=poacher11)
poacher2 = trtl.Turtle(shape=poacher22)
poacher3 = trtl.Turtle(shape=poacher33)
poacher4 = trtl.Turtle(shape=poacher44)
hippo = trtl.Turtle(shape=hippo1)

for p in [poacher1, poacher2, poacher3, poacher4]:
    p.penup()
    p.speed(0)
hippo.penup()
hippo.speed(0)


#--score-------------------------------------
score = 0
font_setup = ('Arial',30,'normal')
score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(-20,165)
score_writer.pendown()
score_writer.write(score,font=font_setup)
score_writer.hideturtle()
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#counter wirter----------------------------
counter =  trtl.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(70,170)
#-----game functions--------

def change_score():
    global score 
    score += 1
    score_writer.clear()
    score_writer.write(score,font=font_setup)
    
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    manage_leaderboard()
    spot.hideturtle()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

# manages the leaderboard for top 5 scorers
def manage_leaderboard():

  global score
  # get the names and scores from the leaderboard file
  leader_names_list = lb.get_names(leaderboard_file_name)
  leader_scores_list = lb.get_scores(leaderboard_file_name)

  # show the leaderboard with or without the current player
  if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(True, leader_names_list, leader_scores_list, hippo, score)

  else:
    lb.draw_leaderboard(False, leader_names_list, leader_scores_list, hippo, score)

#--hippo move---
def move_up():
  y= hippo.ycor()
  if y < 200:
    hippo.sety(y + 30)

def move_down():
    y = hippo.ycor()
    if y > -200:
        hippo.sety(y - 30)

#--shoot---
bullet = trtl.Turtle()
bullet.shape('circle')
bullet.color('red')
bullet.penup()
bullet.hideturtle()
bullet.speed(0)

def shoot():
  if not bullet.invisible(): #only shoots one bullet 
    bullet.setx(bullet.xcor() -20)
    #check if shot
    for poacher in [poacher1,poacher2, poacher3,poacher4]:
      if bullet.distance(poacher) <30:
        bullet.hideturtle()
        poacher.goto(-225,rand.randint(-150,150))
        change_score()
        return
    wn.ontimer(move_bullet,50)
  else:
    bullet.hideturtle

#-----poacher placement-----
poacher1.goto(-225,150)
poacher2.goto(-225,50)
poacher3.goto(-225,-50)
poacher4.goto(-225,-150)

hippo.goto(225,0)
hippo.showturtle()

#-----keyboard bindings-----
wn.listen()
wn.onkeypress(move_up, "Up")
wn.onkeypress(move_down, "Down")
wn.onkeypress(shoot, "space")



wn.ontimer(countdown, counter_interval) 
wn.bgpic("background.gif")
wn.setup(width=848, height=539)
wn.mainloop()