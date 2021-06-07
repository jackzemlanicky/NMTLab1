'''
This program reads in a PDF file, converts it into an integer array (from the ASCII values of the bytes)and generates a grayscale image based on the integers of the integer array, one pixel per byte/integer
Author: Jack Zemlanicky
Contributors: Bill Luo
'''
import array as arr
from PIL import Image
from numpy import ceil, sqrt

# variables


# functions

# Pad extra zeroes to get to the next square (for the image)
def pad_zeroes(int_array):
    while int_array.__len__()<width**2:
        int_array.append(0)

# Given the size of the file, find the next square number 
def find_next_square(size):
    # ceiling value so it is always >= the size of the file, never smaller
    return int(ceil(sqrt(size)))

# Initialize our integer array
int_array= arr.array('i')
# Get the file as a byte stream
pdfFile = open('Sample.pdf','rb')
# Get the array of bytes from the stream
byteArray = pdfFile.read()
# Put the individual bytes (ascii values) into an array
for byte in byteArray:
    int_array.append(byte)
# Now, all values in int_array are between 0 and 255, each one representing a single byte from the pdf file
# Get the size of our grayscale image based on the size of the PDF
width=find_next_square(int_array.__len__())
print(width)
print(type(width))
# Pad on appropriate amount of zeroes to the image
pad_zeroes(int_array)

# Create our image in grayscale, 8 bits per pixel
img = Image.new('L',(width,width))
img.putdata(int_array)
img.save('plswork.png')
pdfFile.close()
