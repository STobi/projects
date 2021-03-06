# CAN BE RUN HERE: http://www.codeskulptor.org/#user47_2F57Hxdw5D_7.py

# Implementation of classic arcade game Pong

import simplegui
import random
import math

# initialize globals - pos and vel encode vertical info for paddles

WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0 / 20,  0 / 20]


# initialize ball_pos and ball_vel for new ball in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
# The ball spawns moving towards the player that won the last point
def spawn_ball(direction):
    global ball_pos, ball_vel, ball_acc # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if direction:
        ball_vel = [(random.randrange(120, 240) / 60), ((random.randrange(60, 180) / 60) * -1)]
    else:
        ball_vel = [((random.randrange(120, 240) / 60) * -1), ((random.randrange(60, 180) / 60) * -1)]
        
    
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    paddle1_pos = HEIGHT / 2
    paddle2_pos = HEIGHT / 2
    paddle1_vel = 0
    paddle2_vel = 0
    score1 = 0
    score2 = 0
    spawn_ball(LEFT)
    

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel, ball_acc
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # collide and reflect top and bottom of canvas
    if ball_pos[1] <= (BALL_RADIUS):
        print ball_pos
        ball_vel[1] = - ball_vel[1]
    elif ball_pos[1] >= (HEIGHT - BALL_RADIUS):
        ball_vel[1] = - ball_vel[1]
    elif ball_pos[1] <= ((HEIGHT - BALL_RADIUS) * -1):
        ball_vel[1] = - ball_vel[1]
    
    # draw ball
    canvas.draw_circle((ball_pos), BALL_RADIUS, 2, "White", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    if (paddle1_pos + paddle1_vel >= HALF_PAD_HEIGHT) and (paddle1_pos + paddle1_vel <= HEIGHT - HALF_PAD_HEIGHT):
        paddle1_pos += paddle1_vel
    else: 
        paddle1_vel = 0
    if (paddle2_pos + paddle2_vel >= HALF_PAD_HEIGHT) and (paddle2_pos + paddle2_vel <= HEIGHT - HALF_PAD_HEIGHT):
        paddle2_pos += paddle2_vel
    else: 
        paddle2_vel = 0
    
    # draw paddles
    canvas.draw_line([(WIDTH - HALF_PAD_WIDTH),((paddle1_pos) + HALF_PAD_HEIGHT)], [(WIDTH - HALF_PAD_WIDTH), ((paddle1_pos) - HALF_PAD_HEIGHT)], PAD_WIDTH, "White")
    canvas.draw_line([(HALF_PAD_WIDTH),((paddle2_pos) + HALF_PAD_HEIGHT)], [(HALF_PAD_WIDTH), ((paddle2_pos) - HALF_PAD_HEIGHT)], PAD_WIDTH, "White")
    
    ## Determine if ball collides with paddle or gutter
    # Left Paddle (Player 2)
    if (ball_pos[0] <= (BALL_RADIUS + PAD_WIDTH)) and ((paddle2_pos - HALF_PAD_HEIGHT - 2) <= ball_pos[1] <= (paddle2_pos + HALF_PAD_HEIGHT + 2)):
        ball_vel[0] += ball_vel[0] * 0.1
        ball_vel[0] = - ball_vel[0]
    elif ball_pos[0] < (BALL_RADIUS + PAD_WIDTH):
        spawn_ball(RIGHT)
        score2 += 1
    # Right Paddle (Player 1)
    if (ball_pos[0] >= (WIDTH - BALL_RADIUS - PAD_WIDTH)) and ((paddle1_pos - HALF_PAD_HEIGHT - 2) <= ball_pos[1] <= (paddle1_pos + HALF_PAD_HEIGHT + 2)):
        ball_vel[0] += ball_vel[0] * 0.1
        ball_vel[0] = - ball_vel[0]
    elif ball_pos[0] > (WIDTH - BALL_RADIUS - PAD_WIDTH):
        spawn_ball(LEFT)
        score1 += 1
    elif ball_pos[0] < ((WIDTH - BALL_RADIUS - PAD_WIDTH) * -1):
        spawn_ball(LEFT)
        score1 += 1
        
    # draw scores
    canvas.draw_text(str(score1), (WIDTH / 2 * 0.75, HEIGHT * 0.25), 50, "Green")
    canvas.draw_text(str(score2), (WIDTH / 2 + 50, HEIGHT * 0.25), 50, "Green")
        
def keydown(key):
    acc = 2.5
    #Player 1 up and down paddle control
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["up"]:
        paddle1_vel -= acc
    elif key == simplegui.KEY_MAP["down"]:
        paddle1_vel += acc
    #Player 2 up and down paddle control
    if key == simplegui.KEY_MAP["w"]:
        paddle2_vel -= acc
    elif key == simplegui.KEY_MAP["s"]:
        paddle2_vel += acc
        
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    #Player 1 up and down paddle control
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["up"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["down"]:
        paddle1_vel = 0
    #Player 2 up and down paddle control
    if key == simplegui.KEY_MAP["w"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["s"]:
        paddle2_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
restart = frame.add_button("Restart", new_game)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
