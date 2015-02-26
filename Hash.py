'''
# Created by Ethan Richardson, Nathan Knight
# written for Python3

You are required to implement in Python a very simple hash function 
(that is meant more for play than for any serious production work). 
Write a function that creates a 32-bit hash of a file 
(you can represent 32-bits in hexadecimal and use it as the output for simplicity) 
through the following steps:
See GitHub for prompt

'''
#!/usr/bin/env python
import sys

from BitVector import *
from glob import *

def main():

	#INCOMPLETE
	###########################
	#Scan your directory (current), compute the hash of all your files.
	dirScan = glob('*.*')
	fileCount = 0

	###########################

	#Wrap for each file
	
	#testFile.txt
	bv = BitVector(filename = dirScan[4])
	
	#Initialize the hash to all zeros.
	#This bit vector will hold exactly 32 bits, all initialized to the 0 bit value.
	myHash = BitVector(size = 32)
	
	#If no more data to read,
	#Stop after shifting
	while (bv.more_to_read):
		#Scan the file one byte (8bits) at a time.
		bv1 = bv.read_bits_from_file(8)
		print("orig:",bv1)	
		
		#XOR the new byte read from the file with 
		#the least significant byte (the rightmost) of the hash.
		myHash[0:8] = bv1 ^ myHash[0:8]
		
		#Circularly shift bit pattern in hash to left by 8 pos.
		myHash << 8
		print("shft:", myHash)
	
	bv.close_file_object()
		
	#Convert to Hex
	print (myHash.getHexStringFromBitVector())

	'''
	#Dump the hash values in some output file.
	dumpFile = open('dump.txt', 'wb')
	bv1.write_to_file(dumpFile)
	dumpFile.close()
	'''

main()