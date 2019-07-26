# 2.5 Sum Lists: You have two numbers represented by a linked list, 
# where each node contains a single digit. The digits are stored in reverse order, 
# such that the 1's digit is at the head of the list. Write a function that adds 
# the two numbers and returns the sum as a linked list.


# EXAMPLE
# Input: (7-> 1 -> 6) + (5 -> 9 -> 2) .# That is:617 + 295. 
# Output:2 -> 1 -> 9.That is:912.

# FOLLOW UP
# Suppose the digits are stored in forward order. Repeat the above problem.
# Input: (6 -> 1 -> 7) + (2 -> 9 -> 5).Thatis,617 + 295. 
# Output:9 -> 1 -> 2.      That is:912.

class Node():
	def __init__(self, data, next=None):
		self.data = data
		self.next = next 


def printList(list1):
	while list1:
		print(list1.data)
		printList(list1.next)


def reverseList(list1):
	return None

def convertListInt(list1):
	str1 = ""
	num1 = 0
	p1 = list1
	while p1:
		str1 += str(p1.data)
		p1 = p1.next
	num1 = int(str1)
	print(num1) 	
	return num1

def convertIntList(num1):
	str1 = str(num1)
	list1 = Node(str1[0])

	for i in range(1,len(str1)):
		list1.data = str1[i]
		list1.next = Node(0)

	printList(list1)
	return list1	


def sumList(list1, list2):
	reverseList(list1)
	reverseList(list2)
	num1 = convertListInt(list1)
	num2 = convertListInt(list2)
	list3 = convertIntList(sum(num1+num2))
	# printList(list3)
	# return list3


#Start

list1 = Node(7,Node(1,Node(6)))
list2 = Node(5,Node(9,Node(2)))

sumList(list1, list2)

