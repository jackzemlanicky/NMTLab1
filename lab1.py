import numpy

# Get the file as a byte stream
intArray=[]
pdfFile = open('Sample.pdf','rb')
print(type(pdfFile))
# Get the array of bytes from the stream
byteArray = pdfFile.read()
# Print out whole file (in this case, it is a blank pdf so just header info)
print(byteArray)
# When I print it one character at a time, it gives me the ascii value (an int) but printing anything more than one character gives me the actual text
print(byteArray[0])
# Print length of the file (in bytes)
print(len(byteArray))


pdfFile.close()