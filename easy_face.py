import face_recognition
import cv2
import threading




class Cam:
	def __init__(self,index):
		self.cap = cv2.VideoCapture(index)

	def get_frame(self):
		ret, frame = self.cap.read()
		return frame

class face_proccesing:
	def __init__(self,cam):
		self.known_face_encoding =[]
		self.known_face_name = []
		self.cam = cam
	
	def add_face(self,pic,name):
		image = face_recognition.load_image_file(pic)
		encoding = face_recognition.face_encodings(image)[0]
		self.known_face_name.append(name)
		self.known_face_encoding.append(encoding)
		
	
	def find_face(self,frame):
		#frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25) #Uncomment this line to reduce the size of frame
		face_locations = face_recognition.face_locations(frame)
		face_encodings = face_recognition.face_encodings(frame, face_locations)

	# Loop through each face found in the frame
		for face_encoding in face_encodings:
			# Compare the face with known faces
			matches = face_recognition.compare_faces(self.known_face_encoding, face_encoding)
			name = "Unknown"

		# Find the best match
			if True in matches:
				first_match_index = matches.index(True)
				name = self.known_face_name[first_match_index]
			print(name) #Use this variable to get the name of face	





if __name__ == "__main__":
	pass
