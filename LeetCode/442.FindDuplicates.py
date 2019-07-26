# 442. Find All Duplicates in an Array
# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
# Find all the elements that appear twice in this array.
# Could you do it without extra space and in O(n) runtime?

# Example:
# Input:
# [4,3,2,7,8,2,3,1]

# Output:
# [2,3]


def findDuplicates(nums): #with a map/dictionary
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    # nums.sort().  
    # Runtime: 324 ms, faster than 91.08% of Python online submisions
    mapa = {}
    return_list = []
    for num in nums:
        if num in mapa:
            mapa[num] += 1          
        else:
            mapa[num] = 1
    for num in mapa:
        if mapa[num] > 1:
            return_list.append(num)    
    return return_list


def findDuplicates2(nums): #with no extra space in o(n)
    nums.sort()
    return_list = [-1]
    previus = -2
    for actual in nums:
        if previus == actual and return_list[-1] != actual:
            return_list.append(actual)
        else:
            previus = actual
    return_list.pop(0)
    return return_list



#Start

nums = [2,2,1,3,4,7,2,10,4] #expected [2,4]

# nums = [0]
# nums = [1,1,0,0]
print (findDuplicates(nums))