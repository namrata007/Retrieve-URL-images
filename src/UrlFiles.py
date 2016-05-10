#! usr/bin/python3.4
# This program downloads images from the urls given explicitly in a textfile
from urllib.request import urlopen
from shutil import copyfileobj
import datetime

urlfile = 'urlfile.txt'  # Store the textfile name in a variable
i = 0  # Initialize a counter to number the images downloaded

start = datetime.datetime.now()
furl = open(urlfile)  # Open the file to read
for line in furl:
	if line.startswith('http://') :  # Check if it is a url
		imagefile = 'image_' + str(i)  # Name the image file to be stored
		i += 1  # Increment the counter
		with urlopen(line) as in_stream, open(imagefile, 'wb') as out_file:  # Read the url and open the image file for writing
			copyfileobj(in_stream, out_file)  # Copy the url image to the image file 
		out_file.close()  # Close the image file
end = datetime.datetime.now()
print("\nTime taken\t %.2f", end - start)
        
