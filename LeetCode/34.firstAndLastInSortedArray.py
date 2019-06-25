# 34. Find First and Last Position of Element in Sorted Array
# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
# Your algorithm's runtime complexity must be in the order of O(log n).
# If the target is not found in the array, return [-1, -1].

# Example 1:
                # Input: nums = [5,7,7,8,8,10], target = 8
                # Output: [3,4]
# Example 2
                # Input: nums = [5,7,7,8,8,10], target = 6
                # Output: [-1,-1]
#works OK (faster than 46%)
#TODO: implement with a single binary search function
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/discuss/14713/Search-for-the-position-target-0.5-and-target%2B0.5-a-simple-python-code-with-a-little-trick
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/discuss/271437/Simple-Python-solution-with-binary-search
def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # pos = []
    
    # pos.append(binarySearch(nums,target))


    # # for i in range(len(nums)):
    #     # if target == nums[i]:
    #         # pos.append(i)
    
    # if len(pos) == 1:
    #     pos.append(pos[0])
    # if not pos:
    #     answer =  [ -1, -1]  
    # print(pos[0], pos[int(len(pos)-1)])
    # answer = [ pos[0], pos[int(len(pos) - 1)]]
    # return answer
    
    

def searchRange( nums, target):

        
    left, right = binarySearchLeft(nums, target), binarySearchRight(nums, target)
    return (left, right) if left <= right else [-1, -1]


def binarySearchLeft(A, x):
    left, right = 0, len(A) - 1
    while left <= right:
        mid = (left + right) // 2
        if x > A[mid]: 
            left = mid + 1
        else:
            right = mid - 1
    return left


def binarySearchRight(A, x):
    left, right = 0, len(A) - 1
    while left <= right:
        mid = (left + right) // 2
        if x >= A[mid]:
            left = mid + 1
        else:
            right = mid - 1 
    return right


#Start
      # 0 1 2 3 4 5 6 7 
nums = [5,7,7,8,8,8,8,8] 
nums2 = [1,2,8,8,8,8,8,10] 
target = 8








print(searchRange(nums, target))
print(searchRange(nums2, target))
    