# 2.1 Remove Dups: Write code to remove duplicates from an unsorted linked list. FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?

####Follow Up: No Buffer Allowed####

# I think runtime is O(NlogN)  book says O(N2) and space is O(1)
def removeDuplicated(head):
	node = head
	while node != None:
		runner_node = node
		while runner_node.next != None:
			print("node:{} next:{}" .format(node.data, runner_node.data))#		
			# print("node:{} next:{}" .format(node.next.data, runner_node.data))#		
			if runner_node.next.data == node.data:
				runner_node.next = runner_node.next.next
			else:
				runner_node = runner_node.next
		node = node.next	
	return head		

def printList(head):
	if head != None:
		print (head.data)
		printList(head.next)

# def createLinkedlist(head, list1):	
# 	node = head
# 	print(head.data)
# 	print(node.data)
# 	for num in list1:
# 		node.data = num
# 		node = node.next
# 	node.data = None

#Define Node Class		

class Node():
  def __init__(self, data, next):
    self.data = data
    self.next = next

#Start
# Data 1,2,3,3,5,6,4,2,3,1
# After 1,2,3,5,6
linked_list = Node(1, Node(2,Node(3,Node(5,Node(6,Node(4,Node(4,Node(3,Node(4,None)))))))))

#Create list - Not working now
# linked_list2 = Node(0,None)
# list1 = [1,2,3,4,5,6,7]
# createLinkedlist(linked_list2, list1)
# printList(linked_list2)


printList(linked_list)
removeDuplicated(linked_list)
printList(linked_list)

# print()

