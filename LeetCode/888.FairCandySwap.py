# 888. Fair Candy Swap


# Alice and Bob have candy bars of different sizes: A[i] is the size of the i-th 
# bar of candy that Alice has, and B[j] is the size of the j-th bar of candy that Bob has.
# Since they are friends, they would like to exchange one candy bar each so that 
# after the exchange, they both have the same total amount of candy.  
# (The total amount of candy a person has is the sum of the sizes of candy bars they have.)
# Return an integer array ans where ans[0] is the size of the candy bar that Alice must 
# exchange, and ans[1] is the size of the candy bar that Bob must exchange.
# If there are multiple answers, you may return any one of them.  
# It is guaranteed an answer exists.

# Example 1:

# Input: A = [1,1], B = [2,2]
# Output: [1,2]
# Example 2:

# Input: A = [1,2], B = [2,3]
# Output: [1,2]
# Example 3:

# Input: A = [2], B = [1,3]
# Output: [2,3]
# Example 4:

# Input: A = [1,2,5], B = [2,4]  8, 6
# Output: [5,4]
 

# Note:

# 1 <= A.length <= 10000
# 1 <= B.length <= 10000
# 1 <= A[i] <= 100000
# 1 <= B[i] <= 100000
# It is guaranteed that Alice and Bob have different total amounts of candy.
# It is guaranteed there exists an answer.


def candySwap(kid1, kid2):
	candy1 = sum(kid1)
	candy2 = sum(kid2)	
	average = (candy1 + candy2) / 2
	diff = (candy2 - candy1) / 2
	print("diff:", diff)
	for item in kid1:
		target = item + diff 
		print("target:", target)
		if target in kid2:
			 return [item, target]


def candySwap2(A, B):
	flagABig = False
	i = 0
	j = 0
	if sum(A)>sum(B):
		flagABig = True
	if flagABig:
		diff = (sum(A)-sum(B))/2
		A = set(map(lambda x: x - diff, A))
		print(A)
		B = set(B)
		val = (A&B).pop()

		return [val+diff,val]
	else:
		diff = (sum(B)-sum(A))/2
		A = set(A)
		B = set(map(lambda x: x - diff, B))
		print(B)
		val = (A&B).pop()
		return [val,val+diff]




# Start

A = [5,1,2]
B = [4,2] 		# 8, 6 [5,4]

print(candySwap2(A,B))




