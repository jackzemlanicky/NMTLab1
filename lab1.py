'''
This program reads in a PDF file, converts it into an integer array (from the ASCII values of the bytes)and generates a grayscale image based on the integers of the integer array, one pixel per byte/integer
Author: Jack Zemlanicky
Contributors: Bill Luo
'''
import array as arr
from PIL import Image

# variables

# The final value for our square, set the initial square to 25 (blank pdf file is about 800 bytes)
# Confused as to how I can update this global variable from inside the while loop in my find_next_square function
final_square = 25
# functions

# Pad extra zeroes to get to the next square (for the image)
def pad_zeroes(int_array):
    while int_array.__len__()<final_square*final_square:
        int_array.append(0)

# Given the size of the file, find the next square number 
def find_next_square(size,final_square):
    while size<final_square*final_square:
        final_square+=1
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
find_next_square(int_array.__len__(),final_square)
# Pad on appropriate amount of zeroes to the image
pad_zeroes(int_array)


img = Image.new('L',final_square,final_square)
img.putdata(int_array)
img.save('plswork.png')
pdfFile.close()
