# Program To Read video 
# and Extract Frames 

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2 
import os
import sys, termios, tty, os, time, threading

#global variables
count = 0
imgName = ""
sort = False
key = 0

# Function to extract frames 
def run():
    FrameCapture(path)


def FrameCapture(path): 
    global count
    global key

    orig_settings = termios.tcgetattr(sys.stdin)
    tty.setraw(sys.stdin)
    x = 0
      
    # Path to video file 
    vidObj = cv2.VideoCapture(path) 
  
    # checks whether frames were extracted 
    success = 1

  
    while success: 
  
        # vidObj object calls read 
        # function extract frames 
        success, image = vidObj.read() 
  
        # Saves the frames with frame-count 
	if count%5==0:
        	cv2.imwrite("frame_%d.jpg" % count, image) 
		imgName = "frame_" + str(count) + ".jpg"
		img=mpimg.imread(imgName)
		imgplot = plt.imshow(img)
		plt.show()
		if key == "1":
		    print("RAT")
		elif key =="2":
		    print("NO RAT")
		plt.close('all') 
  
        count += 1

	#for x in range (0,count,5):
		#img=mpimg.imread(imgName)
		#imgplot = plt.imshow(img)
		#plt.show()  

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
 
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch
 
button_delay = 0.2

def keys():
    global sort
    global key 

    while True:
	char = getch()

	if (char == "p"):
	    print("Stop!")
	exit(0)

	if (char == "1"):
	    print("rat")
	    sort = True
            key = char
	    time.sleep(button_delay)

	elif (char == "2"):
	    print("no rat")
	    sort = True
            key = char
	    time.sleep(button_delay)


  
# Driver Code 
if __name__ == '__main__': 
    path = os.path.expanduser('~/Desktop/sandbox/research/RatVideos/my_video-14.mp4')
    # Calling the function 
    FrameCapture(path) 

keyboard = threading.Thread(target = keys)
gestureLoop = threading.Thread(target = run)

keyboard.start()
gestureLoop.start()

keyboard.join()
gestureLoop.join()

