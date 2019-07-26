# Partition: Write code to partition a linked list around a value x, 
# such that all nodes less than x come before all nodes greater than 
# or equal to x. If x is contained within the list, the values of x 
# only need to be after the elements less than x (see below). 
# The partition element x can appear anywhere in the "right partition"; 
# it does not need to appear between the left and right partitions.

# SOLUTION
# EXAMPLE
# Input: 	3 -> 5 -> 8 ->  5 -> 10 -> 2 -> 1 [partition=5] 
# Output: 	3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8


class Node():
	def __init__(self, data, next=None):
		self.data = data
		self.next = next


def partitionNode(head, target):
	pl1, pl2, pr1, pr2 = None, None, None, None

	# listL = Node(None, None) # how to create a new node?
	# listH = Node(None, None) 

	node = head

	while node:
		if node.data < target: #send to Left list
			# listL.data = head.data
			# listL.next = 
			if pl1:
				pl2.next = node
				pl2 = node
			else:
				pl1 = node
				pl2 = node
		else:

			if pr1:
				pr2.next = node
				pr2 = node
			else:
				pr1 = node
				pr2 = node
		node = node.next
	pl2.next = pr1	#Merging the two lists

	return pl1

def printList(head):
	if head.next:
		print(head.data)
		printList(head.next)



    # string = str(head.data)
    # if head.next:
    #   string += ',' + str(head.next)
    # print( str(string))





#Start

list1 = Node(3,Node(5,Node(8,Node(5,Node(10,Node(2,Node(1)))))))
# expected Output: 	3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8



printList(partitionNode(list1, 5))


# print(str(partitionNode(list1, 5)))

