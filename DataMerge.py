import os

files = [
	'data/data0.txt',
	'data/data1.txt',
	'data/data2.txt',
	'data/data3.txt',
	'data/data4.txt',
	'data/data5.txt',
	'data/data6.txt',
]

fileMerged = 'data/merged.txt'
fileTemp = 'data/temp.txt'

def getSortedData(path):
	file = open(path, 'r')
	ret = []
	while True:
		line = file.readline()
		if not line:
			break
		ret.append(line)
	ret.sort()
	return ret

def mergeData(dataList):
	fileIn = open(fileMerged, 'r')
	fileOut = open(fileTemp, 'w')

	index = 0
	while True:
		line = fileIn.readline()
		if not line:
			break
		while index < len(dataList) and dataList[index] < line:
			fileOut.write(dataList[index])
			index += 1
		fileOut.write(line)

	while index < len(dataList):
		fileOut.write(dataList[index])
		index += 1

	fileIn.close()
	fileOut.close()
	os.remove(fileMerged)
	os.rename(fileTemp, fileMerged)

def removeDuplicate():
	fileIn = open(fileMerged, 'r')
	fileOut = open(fileTemp, 'w')

	last = None
	while True:
		line = fileIn.readline()
		if not line:
			break
		if line == last:
			continue
		fileOut.write(line)
		last = line

	fileIn.close()
	fileOut.close()
	os.remove(fileMerged)
	os.rename(fileTemp, fileMerged)


for filePath in files:
	sortedData = getSortedData(filePath)
	mergeData(sortedData)
removeDuplicate()
