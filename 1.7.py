# 1.7 Rotate Matrix: Given an image represented by an NxN matrix, 
# where each pixel in the image is 4 bytes, write a method to rotate the image by 
# 90 degrees. Can you do this in place?


def rotate90(matrix):
	new_matrix = []
	for M in range(len(matrix)):
		row = []
		for N in range (len(matrix[M])):
			# row.append(matrix[M][4 - N])
			inver_index = int(len(matrix[M])) - N -1
			# print("inver_index" , inver_index)
			# row.append(matrix[N][M])
			# row.append(matrix[N][int(inver_index)])
			row.append(matrix[int(inver_index)][M])

			# print (matrix[M][N])
		new_matrix.append(row)

		# print(N)
		# print (matrix[N,M])
	print (matrix)
	print (new_matrix)

	return (new_matrix)

#Start 

# Matrix = []
# for i in range(4):
# 	row = []
# 	for j in range(4):
# 		row.append(j)	
# 	Matrix.append(row)	


Matrix2 = [
	("A1", "A2", "A3", "A4"),
	("B1", "B2", "B3", "B4"),
	("C1", "C2", "C3", "C4"),
	("D1", "D2", "D3", "D4")
]

Matrix3 = [
	("FFA1", "FFA2", "FFA3", "FFA4"),
	("FFB1", "FFB2", "FFB3", "FFB4"),
	("FFC1", "FFC2", "FFC3", "FFC4"),
	("FFD1", "FFD2", "FFD3", "FFD4")
]

# rotate90(Matrix)
print("--"*20)
rotate90(Matrix2)
print("--"*20)
rotate90(rotate90(Matrix2))


