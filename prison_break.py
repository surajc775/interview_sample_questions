
def main(xSize, ySize, hValues, vValues):

	xPointStr=""
	yPointStr=""

	rowSize = xSize + 1
	colSize = ySize + 1

	for xPoint in range(rowSize):
		for yPoint in range(colSize):
			xPointStr += str(xPoint)
			yPointStr += str(yPoint)
	
	#print (xPointStr, yPointStr)

	for num in hValues[::-1]:
		xPointStr = xPointStr.replace(str(num), str(num-1))

	for num in vValues[::-1]:
		yPointStr = yPointStr.replace(str(num), str(num-1))

	xyPointAry = []
	xyFrqAry = []

	for num in range(rowSize * colSize):
		xyPoint = xPointStr[num] + yPointStr[num]

		try:
			idx = xyPointAry.index(xyPoint)
			xyFrqAry[idx] = xyFrqAry[idx] + 1
		except ValueError:
			xyPointAry.append(xyPoint)
			xyFrqAry.append(1)
			
	print("Area of the biggest hole = ", max(xyFrqAry))

	'''
	xyPointsAry = []
	for num in range(rowSize * colSize):
		xyPointsAry.append(xPointStr[num] + yPointStr[num])
	#print (xyPointsAry)


	#xyUniqueAry =  [(xyPointsAry.count(xyPt)) for xyPt in xyPointsAry]

	#print("element values = ", xyUniqueAry)
	#print("Area of the biggest hole = ", max(xyUniqueAry))

	maxArea = 1
	for xyPt in xyPointsAry:
		curVal = xyPointsAry.count(xyPt)
		if (curVal > maxArea):
			maxArea = curVal
	print("Area of the biggest hole = ", maxArea)
	'''


if __name__ == "__main__":
	#hor = [2, 4, 6]
	#ver = [11, 12, 15, 19]

	#main(10, 20, hor, ver)

	hor = [2, 4, 6, 66, 54, 55, 56, 57, 58, 59, 82, 94]
	ver = [11, 12, 15, 19, 45, 46, 102, 132, 133, 134]

	main(100, 200, hor, ver)

	# do this to time the program execution in linux
	#	> $ time python yourprogram.py


