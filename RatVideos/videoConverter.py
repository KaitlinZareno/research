# Program To Read video 
# and Extract Frames 

import cv2
import os

cap = cv2.VideoCapture('my_video-14.mp4')
count =0
name = ""

while(cap.isOpened()):
    ok, frame = cap.read()
    #every 5 frames of the video are classified and displayed
    if (count %5 ==0):
	    #create a new jpg file of the current frame
	    cv2.imwrite("frame_%d.jpg" % count, frame) 
	    name = "frame_" + str(count) + ".jpg"
	    cv2.imshow(name , frame)
	    # the 0 in waitKey makes it wait for a keypress before advancing.
	    # if the key is 'q' it quits out of the program. any other key advances to 		      next frame.
	    # after every key pressed, get rid of the current image displaying and display 		      the next image that needs to be classified
	    k = cv2.waitKey(0) & 0xff
	    if k == ord('q'):
		print("quit")
		break
	    #if k == ord('r'):
		#print("r pressed")
		#cv2.destroyAllWindows()
	    if k == ord('1'):
		# "./" look in the same directory and concatnate the name of the current 			   frame in order to classify 
		os.rename("./"+name, "./rat2/"+name)
		print("image moved to rat2 directory")		
		cv2.destroyAllWindows()
	    if k == ord('2'):
		print("image moved to no_rat2 directory")
		os.rename("./" +name, "./no_rat2/" +name)
		cv2.destroyAllWindows()
    count+=1

cap.release()
cv2.destroyAllWindows()

