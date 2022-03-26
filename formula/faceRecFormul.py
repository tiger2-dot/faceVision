import cv2 #pip install opencv-python
import numpy as np #pip isntall numpy
import face_recognition #pip isntall cmake -> pip install dlib -> pip install face_recognition
import os


myself = face_recognition.load_image_file("myself.jpg") #load image as black and white

face = face_recognition.face_locations(myself)[0] #find coordinates of main face
start = (face[1],face[0]) #right,top coordinates
end = (face[3],face[2]) #left,bottom coordinates
recColor = (0,0,255) #color in BGR
thickness = 2 #thickness of drawn line
foundFace = cv2.rectangle(myself, start, end, recColor, thickness)


mainFace = face_recognition.face_encodings(face_image = myself)[0] #get encoding of the main face

#use os to iterate throught all images and check in each image if main face exist
path = os.getcwd()
allImg = os.listdir(path)
for img in allImg:
	(name,typ) = img.split('.')
	if typ == 'jpg' or typ == 'png': #we do not want to try and open file that is not image
		if name != 'myself': #we want to ignore ourself
			#check each img
			imag = face_recognition.load_image_file(img) #load image
			faces = face_recognition.face_encodings(face_image = imag) #encode all faces
			dist = face_recognition.compare_faces(faces,mainFace,tolerance = 0.6) #calculate distances for each face
			print (dist)
			print (name)


'''
for a in images:
	print (a) 


cv2.imshow('face',foundFace)
cv2.waitKey(0)
'''