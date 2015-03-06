# SimpleHash
Hash Function Implementation with Python
----------------------------------------
This is a very simple hash function meant more for play than actual production work. This function creates a 32-bit hexidecimal hash dump of a file through the following steps:

 - Initialize the hash to all zeros.
 - Scan the file one byte at a time.
 - Before a new byte is read from the file, circularly shift the bit pattern in the hash to the left by 8 positions.
	* Note that if there is no more data to read, you stop here (i.e., after shifting).
 - XOR the new byte read from the file with the least significant byte (the rightmost) of the hash.
 - Scan your directory (a very simple thing to do in Python), and compute the hash of all your files.
 - Dump the hash values in some output file.
  * Reference: BitVector [https://engineering.purdue.edu/kak/dist/BitVector-3.3.2.html]()
