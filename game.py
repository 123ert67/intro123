import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

# globals
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 10
PAD_HEIGHT = 80
LEFT = False
RIGHT = True

w_pressed = False
s_pressed = False
up_pressed = False
down_pressed = False

single_player = False

ball_pos = [0, 0]
ball_vel = [0, 0]

paddle1_pos = 0
paddle2_pos = 0

paddle1_vel = 0
paddle2_vel = 0

score1 = 0
score2 = 0


def spawn_ball(direction):
    global ball_pos, ball_vel  
    
    ball_pos = [WIDTH // 2, HEIGHT // 2]
    
    vx = random.randrange(120, 240) // 60
    vy = -random.randrange(60, 180) // 60
    
    if direction == LEFT:
        vx = -vx 
    
    ball_vel = [vx, vy]

def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # numbers
    global score1, score2  #int
    
    score1 = score2 = 0
    
    paddle1_pos = HEIGHT // 2 - 10
    paddle2_pos = HEIGHT // 2 - 10

    paddle1_vel = 0
    paddle2_vel = 0
    
    spawn_ball(bool(random.randrange(0,2)))

def paddle_AI():#noob ai
    global paddle2_pos, ball_pos, paddle2_vel
    print(ball_pos[1], paddle2_pos + PAD_HEIGHT // 2)
    if (ball_pos[1] < paddle2_pos + PAD_HEIGHT // 2):
        paddle2_pos -= 4
    elif (ball_pos[1] > paddle2_pos + PAD_HEIGHT // 2):
        paddle2_pos += 4
    else:
        paddle2_vel = 0
    

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel,single_player
        
    # coard
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 3, "purple")	# mid line
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "red")		# gutters
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "green")
    
    canvas.draw_circle([WIDTH / 2, HEIGHT / 2], 85, 4, "Purple")

        
    
    # update ball    
    ball_pos[0] = ball_pos[0] + ball_vel[0]  
    ball_pos[1] = ball_pos[1] + ball_vel[1]        
    
    # physics
    if (ball_pos[1] - BALL_RADIUS <= 0) or (ball_pos[1] + BALL_RADIUS >= HEIGHT):
        ball_vel[1] = -ball_vel[1]
       
    # ball detail
    canvas.draw_circle(ball_pos, BALL_RADIUS, 13, "Purple")
    canvas.draw_circle(ball_pos, BALL_RADIUS, 7, "White") 
    
        
    # update paddle posi
     
    if not (((paddle1_pos + paddle1_vel) <= 0) or ((paddle1_pos + paddle1_vel + PAD_HEIGHT) >= HEIGHT)):
        paddle1_pos = paddle1_pos + paddle1_vel 

    if(single_player):
        paddle_AI()

    else:       
        if not (((paddle2_pos + paddle2_vel) <= 0) or ((paddle2_pos + paddle2_vel + PAD_HEIGHT) >= HEIGHT)):
            paddle2_pos = paddle2_pos + paddle2_vel      
        
    canvas.draw_line([0, paddle1_pos],[0, paddle1_pos + PAD_HEIGHT], PAD_WIDTH, "white")
    canvas.draw_line([WIDTH, paddle2_pos],[WIDTH, paddle2_pos + PAD_HEIGHT], PAD_WIDTH, "white")

    
    # if hit    
    if (ball_pos[0] - BALL_RADIUS) <= PAD_WIDTH:
        
        # deflection
        if ((ball_pos[1] >= paddle1_pos) and (ball_pos[1] <= (paddle1_pos + PAD_HEIGHT))): 
            
            ball_vel[0] = -ball_vel[0]	
            ball_vel[0] += (ball_vel[0] // 10)
            ball_vel[1] += (ball_vel[1] // 10)
            
        else:
            score2 += 1
            spawn_ball(True)

    elif (ball_pos[0] + BALL_RADIUS) >= (WIDTH - PAD_WIDTH):
        
        # deflection   
        if ((ball_pos[1] >= paddle2_pos) and (ball_pos[1] <= (paddle2_pos + PAD_HEIGHT))): 
            
            ball_vel[0] = -ball_vel[0]
            ball_vel[0] += (ball_vel[0] // 10)
            ball_vel[1] += (ball_vel[1] // 10)
            
        else:
            score1 += 1
            spawn_ball(False)
            
    # score
    canvas.draw_text(str(score1), [180, 50], 55, "Red") 
    canvas.draw_text(str(score2), [420, 50], 55, "Lime")         
        
        
def keydown(key):
    global paddle1_vel, paddle2_vel,w_pressed,s_pressed,up_pressed,down_pressed    
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= 4
        w_pressed = True
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel += 4
        s_pressed = True
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= 4
        up_pressed = True
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel += 4
        down_pressed = True
   

def keyup(key):
    global paddle1_vel, paddle2_vel,w_pressed,s_pressed,up_pressed,down_pressed
    
    if (key == simplegui.KEY_MAP["w"]) or (key == simplegui.KEY_MAP["s"]):
        if(key == simplegui.KEY_MAP["w"]):
            w_pressed = False
        elif(key == simplegui.KEY_MAP["s"]):
            s_pressed = False
        if (w_pressed == False) and (s_pressed == False):
            paddle1_vel = 0
        elif(w_pressed == True) and (s_pressed == False):
            paddle1_vel -= 4
        elif(w_pressed == False) and (s_pressed == True):
            paddle1_vel += 4
    elif (key == simplegui.KEY_MAP["up"]) or (key == simplegui.KEY_MAP["down"]):
        if(key == simplegui.KEY_MAP["up"]):
            up_pressed = False
        elif(key == simplegui.KEY_MAP["down"]):
            down_pressed = False
        if (up_pressed == False) and (down_pressed == False):
            paddle2_vel = 0
        elif(up_pressed == True) and (down_pressed == False):
            paddle2_vel -= 4
        elif(up_pressed == False) and (down_pressed == True):
            paddle2_vel += 4

def toggle_mode():
    global single_player
    single_player = not single_player
    
    new_game()
    
    


# render
frame = simplegui.create_frame("Pong Game(NOOB AI Debsirin)", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 100)
frame.add_button("Single Player(vs AI)", toggle_mode, 150)

# start
new_game()
frame.start()