import sys
from glob import *
from BitVector import *
def HashbyGhost():
	dirScan = glob('input/*.*')
	fileCount = 0
	while(fileCount < len(dirScan)):
		bv = BitVector(filename = dirScan[fileCount])
		
		myHash = BitVector(size = 32)
		
		while (bv.more_to_read):
			bv1 = bv.read_bits_from_file(8)
			myHash[0:8] = bv1 ^ myHash[0:8]
			myHash << 8
		
		bv.close_file_object()
		myHexHash = myHash.getHexStringFromBitVector()
		dumpFile = open('output/output.txt', 'a')
		dumpFile.write('\n')
		dumpFile.write(dirScan[fileCount])
		dumpFile.write(":")
		dumpFile.write(myHexHash)
		dumpFile.close()
		fileCount += 1
HashbyGhost()