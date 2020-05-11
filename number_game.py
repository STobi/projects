# Run here: http://www.codeskulptor.org/#user42_4FSRljwMt3_9.py
# Mini Project 2
#"Guess the number" 
# Player has limited chances to correctly guess
# the computer's random number.

import simplegui
import random
import math

secret_number = 0
num_range = 0
n_guess = 0

def new_game():
    #Helper function that starts and restarts game
    global secret_number
    global num_range
    global n_guess
    print
    
    if num_range != 1000:
        secret_number = random.randrange(0, 100)
        n_guess = 7
        print "New game. Range is from 0 to 100"
        print "Number of remaining guesses is 7"
    else: 
        secret_number = random.randrange(0, 1000)
        n_guess = 10
        print "New game. Range is 0 to 1000"
        print "Number of remaining guesses is 10"
        
def range100():
    # button that changes the range to [0,100) and starts a new game. 
    global num_range
    num_range = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game.     
    global num_range
    num_range = 1000
    new_game()
    
def input_guess(guess):
    # Compares guess against secret_number for match
    # Checks n_guess to determine how many turns are left
    global n_guess
    guess = int(guess)
    n_guess -= 1
    
    print
    print "Guess was " + str(guess) + "."
  
    if (guess < secret_number) and (n_guess > 0):
        print "Number of remaining guesses is " + str(n_guess)
        print "Higher"
    elif (guess > secret_number) and (n_guess > 0):
        print "Number of remaining guesses is " + str(n_guess)
        print "Lower"
    elif n_guess <= 0:
        print "Sorry! No more guesses remain"
        print "My number was " + str(secret_number)
        new_game()
    else:
        print "Correct!"
        print "You had " + str(n_guess) + " guesses remaining!"
        new_game()
    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Input your guess", input_guess, 200)

# call new_game 
new_game()
frame.start()
