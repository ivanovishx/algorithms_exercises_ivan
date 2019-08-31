# https://leetcode.com/problems/peak-index-in-a-mountain-array/
# Also solved in c++

# brute force
# def peakIndexInMountainArray(A_list):

# 	n = len(A_list)
# 	i = 0
# 	j = n - 1
# 	# find the max element
# 	while (i<j):
# 		m = i + (j - i)/2
# 		if (A_list[m] < A_list[m+1]):
# 			i = m + 1
# 		else:
# 			j = m			
# 	return i


# with a binary tree

def peakIndexInMountainArray(A):
    left, right = 0, len(A) - 1
    while left < right:
        mid = (left + right) // 2
        if A[mid - 1] < A[mid] and A[mid] < A[mid + 1]:
            left = mid
        elif A[mid - 1] > A[mid] and A[mid] > A[mid + 1]:
            right = mid
        else:
            break
    return mid


#start:

A_list = [0,2,1,0]
print (peakIndexInMountainArray(A_list))










