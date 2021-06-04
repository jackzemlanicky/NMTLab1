import array as arr

# Initialize our integer array
intArray= arr.array('i')
# Get the file as a byte stream
pdfFile = open('Sample.pdf','rb')
print(type(pdfFile))
# Get the array of bytes from the stream
byteArray = pdfFile.read()
# Put the individual bytes (ascii values) into an array
for byte in byteArray:
    intArray.append(byte)
# Save the size of the file in bytes (1 byte = 1 value in the array) for later use
file_size = intArray.__len__()
# Now, all values in intArray are between 0 and 255, each one representing a single byte from the pdf file
pdfFile.close()
