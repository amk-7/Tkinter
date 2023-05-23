import sys

import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
from PIL import Image
import random
import cv2


#sys.path.append('home/amk/Images/')



def main():
	#image = Image.open('test.jpeg')
	#frame = image.face(gray=True)	
	#array = np.asarray(image)
	#print(misc)
	print(toASCII('test.jpeg', 70, 50))
	


def toASCII(fichier, cols=120, rows=35):
	if fichier == misc:
		frame = fichier.face(gray=True)				# Charge l'image en blanc noir
	else:
		image = cv2.imread(fichier)
		frame = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	
	height, width = frame.shape					# Récupérer les dimansions de l'image
	#print(height, width)
	if cols > width or rows > height:
		raise ValueError("Too many cols or rows.")
	cell_width = width / cols					# Quadriller notre image 
	cell_height = height/ rows
	result=""
	for i in range(rows):
		for j in range(cols):
			gray = np.mean(
				frame[int(i * cell_height):min(int((i + 1) * cell_height), height), int(j * cell_width):min(int((j + 1) * cell_width), width)]						# Faire la moyen des pixels dans la case i, j
			)
			result +=grayTochar(gray)
		result += "\n"
		
	return result
	
def grayTochar(gray):
	CHAR_LIST = ' .:-=+*#%@'
	#CHAR_LIST = '@%#*+=-:. '
	num_chars = len(CHAR_LIST)
	return CHAR_LIST[
		min(
		int(gray*num_chars/255), 
		num_chars-1
		)
	]

if __name__=="__main__":
	main()
	#toASCII(misc)
	
