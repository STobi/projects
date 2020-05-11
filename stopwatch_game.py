# RUN HERE: http://www.codeskulptor.org/#user43_Dz5etnQTx9_1.py
# Press start to run the click. Click stop to try and stop on the exact second. Earn a hit or miss based on your reflexes. 
# Mini-Project #3: "Stopwatch: The Game" 

import simplegui

width = 300
height = 200
total_ticks = 0
total_stop = 0
correct_stops = 0
is_running = True


# Helper function: converts time
# in tenths of seconds into formatted string A:BC.D

def format(total_ticks):
    a = total_ticks // 600
    b = ((total_ticks // 10) % 60) // 10
    c = ((total_ticks // 10) % 60) % 10
    d = total_ticks % 10
    return str(a) + ":" + str(b) + str(c) + "." + str(d)

def correct_checker(seconds):
    global correct_stops
    if str(seconds)[-1] == "0":
        return correct_stops + 1
    else:
        return correct_stops
    
# Event handlers for buttons; "Start", "Stop", "Reset"

def start():
    global is_running
    timer.start()
    is_running = True

def reset():
    global total_ticks
    global total_stop
    global correct_stops
    timer.stop()
    total_ticks = 0
    total_stop = 0
    correct_stops = 0
    
def stop():
    global is_running
    global total_ticks
    global total_stop
    global correct_stops
    if is_running:
        timer.stop()
        total_stop += 1
        correct_stops = correct_checker(total_ticks)
        is_running = False
        
# Timer event handler
def tick():
    global total_ticks
    total_ticks += 1

# Draw handler
def draw(canvas):
    canvas.draw_text(str(format(total_ticks)), [(width / 2.75), (height / 1.75)], 35, "White")
    canvas.draw_text(str(correct_stops) + "/" + str(total_stop), [(width / 1.25), (height / 4.5)], 25, "Green")
    
# Frame
frame = simplegui.create_frame("Stopwatch: The Game", width, height)

# Event handlers
frame.set_draw_handler(draw)
frame.add_button("Start", start, 200)
frame.add_button("Stop", stop, 200)
frame.add_button("Reset", reset, 200)
timer = simplegui.create_timer(100, tick)

frame.start()
