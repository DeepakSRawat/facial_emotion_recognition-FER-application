from tkinter import *
from PIL import Image, ImageTk
import cv2 
import imutils
from keras.models import load_model
from time import sleep
from keras.preprocessing.image import img_to_array
from keras.preprocessing import image
import numpy as np
from tkinter import filedialog 

detection_model_path = 'C:/Users/Deepak/Desktop/FACIAL_EMOTION_RECOGNITION/haarcascade_files/haarcascade_frontalface_default.xml'
emotion_model_path = 'C:/Users/Deepak/Desktop/FACIAL_EMOTION_RECOGNITION/models/_mini_XCEPTION.102-0.66.hdf5'
class_labels = ["angry" ,"disgust","scared", "happy", "sad", "surprised","neutral"]

face_classifier = cv2.CascadeClassifier(detection_model_path)
classifier =load_model(emotion_model_path)

#FER main function which recognise function
def FER(frame):
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	faces = face_classifier.detectMultiScale(gray,1.3,5)
	for (x,y,w,h) in faces:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
		roi_gray = gray[y:y+h,x:x+w]
		roi_gray = cv2.resize(roi_gray,(64,64),interpolation=cv2.INTER_AREA)

		if np.sum([roi_gray])!=0:
			roi = roi_gray.astype('float')/255.0
			roi = img_to_array(roi)
			roi = np.expand_dims(roi,axis=0)

		#make a prediction on the RoI, then lookup the class
			preds = classifier.predict(roi)[0]
			# print("\nprediction = ",preds)
			label = class_labels[preds.argmax()]
			# print("\nprediction max = ",preds.argmax())
			# print("\nlabel = ",label)
			label_position = (x,y)
			cv2.putText(frame,label,label_position,cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)
		else:
			cv2.putText(frame,'No Face Found',(20,60),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)
		# print("\n\n")


# FER from video or live 
def visualize():
	global cap
	global clear
	global order
	if order == 1:
		clear.grid(row = 3,column = 0,columnspan = 5)
	if cap is not None:
		ret, frame = cap.read()
		# if i == 1:
		frame = cv2.flip(frame, 1)
		if ret == True:
			# labels = []
			
			FER(frame)

			frame = imutils.resize(frame, width = 610)
			frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
			im = Image.fromarray(frame)
			img = ImageTk.PhotoImage(image = im)

			l_video.configure(image = img)
			l_video.image = img
			l_video.after(10,visualize)
		else:
			l_video.image =""
			cap.release()

# # FER from image
# def visualize_img(cap):
# 	global l_video
# 	# global cap
# 	# l_video.grid_forget()
	
# 	frame = imutils.resize(cap, width = 610)
# 	frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
# 	im = Image.fromarray(frame)
# 	img = ImageTk.PhotoImage(image = im)

# 	l_video.configure(image = img)
# 	l_video.image = img
# 	# l_video = Label(image = cap)
# 	# l_video.grid(row = 0, column = 0, columnspan = 5)

# 	# l_video.after(10,visualize)


# for capturing live video
def initialize():
	global cap
	global order
	global clear
	if order == 1:
		l_video.image = ""
		cap.release()
		cap = None
		clear.grid_forget()
		order = 0
	cap = cv2.VideoCapture(0)
	visualize()

# def finalize():
# 	global cap 
# 	cap.release()

# for uploading video format file
def Upload():
	global cap
	global clear
	global order
	if cap is not None:
		l_video.image = ""
		cap.release()
		cap = None
	filepath = filedialog.askopenfilename(title = "select video", filetype = [
		("all video format",".mp4"),
		("all video format",".avi")])
	if len(filepath) > 0:
		cap = cv2.VideoCapture(filepath)
		order = 1
		visualize()
	else:
		initialize()

# def open_img():
# 	global cap
# 	if cap is not None:
# 		l_video.image = ""
# 		cap.release()
# 		cap = None
# 	filepath = filedialog.askopenfilename(title = "select image", filetype = [
# 		("jpg files","*.jpg"),
# 		("png files","*.png")])
# 	if len(filepath) > 0:
# 		cap = cv2.imread(filepath)
# 		# cap = cv2.VideoCapture(filepath)
# 		visualize_img(cap)
# 	else:
# 		initialize(clear)

root = Tk()

root.title("one eye")

# btnopen = Button(root, text = "open camera", width = 45 ,command = initialize)
# btnopen.grid(column = 0, row = 2, padx = 40, pady = 20, columnspan = 2)

# btnclose = Button(root, text = "close camera", width = 45, command = finalize )
# btnclose.grid(column = 2, row = 2, padx = 5, pady = 5,columnspan = 2)

l_video = Label(root)
l_video.grid(column = 0, row = 0, columnspan = 5)

upload = Button(root, text = "open video", padx = 40, pady = 20, command= Upload)
snap = Button(root, text = "snap", padx = 40, pady = 20, state = DISABLED)
capture = Button(root, text = "capture", padx = 40, pady = 20, state = DISABLED)
emoji = Button(root, text = "emoji", padx = 40, pady = 20, state = DISABLED)
# music = Button(root, text = "music", padx = 40, pady = 20, state = DISABLED)
open_img = Button(root, text = "open image", padx = 40, pady = 20, state = DISABLED)
# exit = Button(root, text = "Exit", padx = 291, pady = 0, fg = "#ff0000", command = root.quit)
clear = Button(root, text = "close", padx = 291, pady = 0, fg = "#ff0000", command = initialize)

upload.grid(row = 1,column = 0)
snap.grid(row = 1,column = 1)
capture.grid(row = 1,column = 2)
emoji.grid(row = 1,column = 3)
# music.grid(row = 1,column = 4)
open_img.grid(row = 1, column = 4)
# exit.grid(row = 3,column = 0,columnspan = 5)
clear.grid_forget()

global order
order = 0
initialize()
root.mainloop()