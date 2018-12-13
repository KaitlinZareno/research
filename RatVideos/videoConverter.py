# Program To Read video 
# and Extract Frames 

import cv2
import os
import argparse

count =0
name = ""
path = ""

parser = argparse.ArgumentParser()
parser.add_argument("--fileloc", help ="path to video you want to convert")
args = parser.parse_args()
parser.add_argument("--dir1", help ="path to first directory/classifier")
args = parser.parse_args()
parser.add_argument("--dir2", help ="path to second directory/classifier")
args = parser.parse_args()

if args.fileloc:
    path = args.fileloc
if args.dir1:
    directory1 = args.fileloc
if args.dir2:
    directory2 = args.fileloc

cap = cv2.VideoCapture(path)
os.makedirs(directory1, exist_ok=True)
os.makedirs(directory2, exist_ok=True)

while(cap.isOpened()):
    ok, frame = cap.read()
    #every 5 frames of the video are classified and displayed
    if (ok == False):
	break
    if (count %5 ==0):
	    #name = "frame_" + str(count) + ".jpg"
	    cv2.imshow("frame" , frame)
	    # the 0 in waitKey makes it wait for a keypress before advancing.
	    # if the key is 'q' it quits out of the program. any other key advances to 		      next frame.
	    # after every key pressed, get rid of the current image displaying and display 		      the next image that needs to be classified
	    k = cv2.waitKey(0) & 0xff
	    if k == ord('q'):
		print("quit")
		break
	    if k == ord('r'):
		print("r pressed")
		#cv2.destroyAllWindows()
	    if k == ord('1'):
		#create a new jpg file of the current frame
	        cv2.imwrite(directory1 + "frame_%d.jpg" % count, frame) 
		print("image moved to " + os.path.basename(directory1) + " 			directory")		
		#cv2.destroyAllWindows()
	    if k == ord('2'):
		print("image moved to " + os.path.basename(directory1) + " directory")
	        #create a new jpg file of the current frame
	        cv2.imwrite(directory2 + "frame_%d.jpg" % count, frame) 
		#cv2.destroyAllWindows()
    count+=1

cap.release()
cv2.destroyAllWindows()

