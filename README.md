# CS410-HW4
Hash Function Implementation with Python
----------------------------------------
You are required to implement in Python a very simple hash function (that is meant more for play than for any serious production work). Write a function that creates a 32-bit hash of a file (you can represent 32-bits in hexadecimal and use it as the output for simplicity) through the following steps:

 - Initialize the hash to all zeros.
 - Scan the file one byte at a time.
 - Before a new byte is read from the file, circularly shift the bit pattern in the hash to the left by 8 positions.
	* Note that if there is no more data to read, you stop here (i.e., after shifting).
 - XOR the new byte read from the file with the least significant byte (the rightmost) of the hash.
 - Scan your directory (a very simple thing to do in Python), and compute the hash of all your files.
 - Dump the hash values in some output file.
  * Hint: You can use BitVector Class