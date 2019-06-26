# 448. Find All Numbers Disappeared in an Array
# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
# Find all the elements of [1, n] inclusive that do not appear in this array.
# Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
# Example:
# Input:
# [4,3,2,7,8,2,3,1]
# Output:
# [5,6]


def findDisappearedNumbers(nums):
	set_compare =  set(range(1,len(nums) + 1))
	# set_compare = set(compare)
	set_nums = set(sorted(nums))

	if len(set_nums) > 0:
		return list(set_compare - set_nums )
	else:
		return []


def findDisappearedNumbers2(nums):
# def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
	#         for i in range(len(nums)):
	#             nums[i] = -nums[i]
	#         for i in range(1,len(nums) + 1):
	for n in nums: 
		nums[abs(n) - 1] = -abs(nums[abs(n) - 1])
	return [i + 1 for i, n in enumerate(nums) if n > 0]



'''
    ret = []
    nums.sort()
    for i in range(len(nums)):
        val = nums[i] - 1
        
        if nums[val] > 0:
            nums[val] = - nums[val]
    for i in range(len(nums)):
        # print(nums[i])
        if nums[i] > 0:
            ret.append(i+1)
        # print (nums[val])
    return ret
  
'''

#Start
nums = [4,3,2,7,8,2,3,1]

print(findDisappearedNumbers2(nums))

