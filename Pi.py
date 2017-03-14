import sys
import os
from PIL import Image
import math

piNumberList = []

def outputImage(diameter):
	r = diameter / 2
	image = Image.new('RGB', (diameter, diameter))
	pixelList = []

	# file containing pi with decimal taken out obtained from https://www.angio.net/pi/digits.html
	filename = 'pi1000000.txt' 

	if os.path.exists(filename):
		with open(filename) as file:
			for line in file:
				for char in line:
					piNumberList.append(char)
		
		# circle plot (x-h)^2 + (y-v)^2 = r^2
		for y in range(0, diameter):
			for x in range(0, diameter):
				currentPixelNumber = round(x + (y * r))

				# check if current pixel is within pythagoras hypotenuse length from centre
				if (math.sqrt((abs(r - x))**2 + (abs(r - y))**2)) < r:
					try:
						pixelList.append(getNumberColor(currentPixelNumber))
					except:
						# if end of file is reached
						print('resolution too high')
						exit()
				else:
					pixelList.append((0, 0, 0))

		image.putdata(pixelList)
		image.show()

	else:
		print('no file')

def getNumberColor(currentPixelNumber):
	colorDict = {'0' : (64, 64, 64),
	'1' : (0, 0, 255),
	'2' : (0, 255, 0),
	'3' : (0, 255, 255),
	'4' : (255, 0, 0),
	'5' : (255, 0, 255),
	'6' : (255, 255, 0),
	'7' : (255, 255, 255),
	'8' : (64, 128, 255),
	'9' : (255, 128, 64)}
	return colorDict[piNumberList[currentPixelNumber]]

if __name__ == '__main__':
	# input is an int declaring circle diameter
	# N.B max resolution is sqrt(2) * sqrt(numberOfDigitsOfPi) i.e. 1000000 digits will have max 1414 pixel diameter
	outputImage(int(sys.argv[1]))