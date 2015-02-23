'''
# Created by Ethan Richardson, Nathan Knight
# written for Python3

You are required to implement in Python a very simple hash function 
(that is meant more for play than for any serious production work). 
Write a function that creates a 32-bit hash of a file 
(you can represent 32-bits in hexadecimal and use it as the output for simplicity) 
through the following steps:


Before a new byte is read from the file, 
circularly shift the bit pattern in the hash to the left by 8 positions.
Note that if there is no more data to read, 
you stop here (i.e., after shifting).
XOR the new byte read from the file with 
the least significant byte (the rightmost) of the hash.
Scan your directory (a very simple thing to do in Python), 
and compute the hash of all your files.

Hint: You can use BitVector Class

'''
#!/usr/bin/env python
import sys

from BitVector import *

def main():
	#Initialize the hash to all zeros.
	#This bit vector will hold exactly 32 bits, all initialized to the 0 bit value.
	bv = BitVector(size = 32)
	
	bv = BitVector( filename = 'testFile.txt' )
	while (bv.more_to_read):
		#Scan the file one byte at a time.
		bv1 = bv_read = bv.read_bits_from_file(32)
		#Circularly shift bit pattern in hash to left by 8 pos.
		bv1 << 8
	print(bv_read)
	
	bv.close_file_object()
	
	'''
	#Scan the file one byte at a time.
	with open("testFile.txt", "rb") as f: #rb+ for read in binary
		nextByte = f.read(1)
		while nextByte:
			#Circularly shift bit pattern in hash to left by 8 pos.
			#bv += nextByte
			bv << 8
			nextByte = f.read(1)
	
	print (bv)
	f.close
	'''
	
	#Dump the hash values in some output file.
	FILEOUT = open( 'output.txt', 'wb' )
	bv1.write_to_file( FILEOUT )
	FILEOUT.close()

	print ("Next Up: Figure out correct method of file access to use.")
	print ("open() or bitVector(filename =), to read ea file in one byte at a time") 
	print ("Make this work with our empty 0-init vector") 

main()