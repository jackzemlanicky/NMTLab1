'''
This program reads in a PDF file, converts it into an integer array (from the ASCII values of the bytes) and generates a grayscale image based on a given width
Author: Jack Zemlanicky
Contributors: Bill Luo
'''
import array as arr
from PIL import Image
from numpy import ceil, sqrt
import cv2

# variables
given_width = 25

# functions

# Pad extra zeroes to get to the next square 
def pad_zeroes(int_array,width):
    while int_array.__len__()<width**2:
        int_array.append(0)

# Given the size of the file, find the next square number 
def find_next_square(size):
    # ceiling value so it is always >= the size of the file, never smaller
    return int(ceil(sqrt(size)))

# Given an int array and width, draw a grayscale image
def draw_image(int_array,width):
    img = Image.new('L',(width,width))
    img.putdata(int_array)
    img.save('grayscale.png')
    pdfFile.close()

# Takes the larger image and scales it down to the given width
def compress_image():
    img = cv2.imread('grayscale.png',cv2.IMREAD_UNCHANGED)
    cv2.resize(img,(given_width,given_width))

# Initialize our integer array
int_array = arr.array('i')
# Get the file as a byte stream
pdfFile = open('Sample.pdf','rb')
# Get the array of bytes from the stream
byteArray = pdfFile.read()
# Put the individual bytes (ascii values) into an array
for byte in byteArray:
    int_array.append(byte)
# If the given width is larger than or equal to the square root of the length of the int array, just pad zeroes then draw the image
if given_width >= sqrt(int_array.__len__()):
    pad_zeroes(int_array,given_width)
    draw_image(int_array,given_width)
# Else the given width is smaller than the sqrt of the length of the array, so we need to first create the image normally, then compress the newly created image to the desired width
else:
    width = find_next_square(int_array.__len__())
    pad_zeroes(int_array)
    draw_image(int_array,width)
    compress_image()
