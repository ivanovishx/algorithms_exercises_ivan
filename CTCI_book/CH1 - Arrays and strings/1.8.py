# 1.8 Zero Matrix: Write an algorithm such that if an element in an MxN 
# matrix is 0, its entire row and column are set to 0.
import unittest
#COMPARE https://github.com/careercup/CtCI-6th-Edition-Python/tree/master/Chapter1/8_Zero%20Matrix
def convert(matrix):
	n = len(matrix)
	m = len(matrix[0])
	
	#I got a problem copyng the array, used list(), .copy(), [:], etc and always is coping the ID
	#so I created a nested for tomanually copy the array in a temp, new copy and fill with matrix
	new_copy = []
	for i in range(n):
		row = []
		for j in range(m):
			row.append(matrix[i][j])
		new_copy.append(row)

	for i in range(n):
		for j in range(m):			
			# print ("i:{}|j:{}|V={}" .format(i,j,matrix[i][j]))
			if new_copy[i][j] == 0:
				for x in range(n):
					matrix[i][x] = 0
					matrix[x][j] = 0
	return matrix
				

#Unit test:
class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ])
    ]

    def test_zero_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = convert(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()


#Start
'''
matrix = [
	[1,1,1,0],
	[1,1,1,1],
	[1,1,1,1],
	[1,1,1,1],
]

print("Original: ",matrix)
print(convert(matrix))

'''