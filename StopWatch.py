This program builds a simple digital stopwatch. 
The stopwatch contain "Start", "Stop" and "Reset" buttons. 

http://www.codeskulptor.org/#user40_9rEY2ZgDH5_1.py
 
import simplegui

# define global variables
nCounter = 0
sTimer, sScore = "", ""
bRunning = False

# define helper function format that converts time
# in tenths of seconds into formatted string Hr:Min:Sec (A:BC:DE.F)
def format(t):
    ndSec = t % 10
    t = t // 10
    nSec2 = t % 10
    t = t // 10
    nSec1 = t % 6
    t = t // 6
    nMin2 = t % 10
    t = t // 10
    nMin1 = t % 6
    nHr = t // 6

    # print "%1d:%1d%1d:%1d%1d.%1d" % (nHr,nMin1,nMin1, nSec1, nSec2, ndSec)
    return str(nHr) + ":" + str(nMin1) + str(nMin2) + ":" + str(nSec1) + str(nSec2) + "." + str(ndSec)


# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global bRunning
    timer.start()
    bRunning = True


def stop():
    global bRunning
    timer.stop()
    bRunning = False


def reset():
    global bRunning, nCounter
    timer.stop()
    nCounter = 0
    bRunning = False


# define event handler for timer with 0.1 sec interval
def tick():
    global nCounter
    nCounter += 1


# define draw handler
def draw(canvas):
    canvas.draw_text(format(nCounter), [35, 85], 36, "Yellow")


# create frame
frame = simplegui.create_frame("Stopwatch", 200, 150)

# register event handlers
frame.add_button("Start", start, 120)
frame.add_button("Stop", stop, 120)
frame.add_button("Reset", reset, 120)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, tick)

# start frame
frame.start()
