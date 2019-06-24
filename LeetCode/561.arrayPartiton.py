# Given an array of 2n integers, your task is to group these integers into 
# n pairs of integer, say (a1, b1), (a2, b2), ..., 
# (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.
# 
# Example 1:
# Input: [1,4,3,2]
# 
# Output: 4
# Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
# Note:
# n is a positive integer, which is in the range of [1, 10000].
# All the integers in the array will be in the range of [-10000, 10000].



def sumMin(nums):# will return sum of all the min pairs sliding the sorted array and computing the sum of min(a+b)
    nums.sort()
    sumMins = 0    
    if(len(nums) >= 2 and not len(nums) % 2 > 0):
        for i in range(len(nums))[::2]:
            sumMins += nums[i] 
        return sumMins
    return False

def arrayPairSum(nums):
	if len(nums) % 2 > 0:
		return False	# is not an even array
	nums.sort()
	return sumMin(nums)


#Start
nums1 = [4,2,1,3,5,6,8,7] #pairs 1-2 3-4 5-6 7-8  mins:  1,3,5,7| sum= 16
nums2 = [4,2,1,3,5,6,0,7] #pairs 0-1 2-3 4-5 6-7  mins:  0,2,4,6| sum= 12

nums3 = [4,2,1,3,5,0] #pairs 0-1 2-3 4-5  mins:  0,2,4| sum= 6



print(arrayPairSum(nums1))
print(arrayPairSum(nums2))
print(arrayPairSum(nums3))




