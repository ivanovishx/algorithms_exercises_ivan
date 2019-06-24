# 2.3 Delete Middle Node: Implement an algorithm to delete a node in the middle 
# (i.e., any node but the first and last node, not necessarily the exact middle) of a singly linked list, given only access to that node.

# EXAMPLE
# Input: the node c from the linked list a->b->c->d->e->f
# Result: nothing is returned, but the new linked list looks like a->b->d->e->f


#TODO: 	-addNode method
#		-lenNode method

class Node():
	def __init__(self, data, next):

		self.data = data
		self.next = next

def printList(head):
	if head:
		print(head.data)
		printList(head.next)

def deleteMiddle(head):
	if not head:
		return None
	p1, p2 = head, head
	counter = 1
	while p1:
		p1 = p1.next
		counter += 1

	if counter % 2 > 0:
		print("is even")
		for i in range(int(counter/2)):
			p2 = p2.next

		p2 = p2.next.next 

		return p2

	else:
		print("is odd")
		return head

def deleteNode(node):
	node = node.next
	node.data = node.next.data

	return node


#Start
ll1 = Node(1,Node(2,Node(3,Node(4,Node(5,None)))))
ll2 = Node(1,Node(2,Node(3,Node(4,Node(5,Node(6,None))))))

print(deleteMiddle(ll1))
print(deleteMiddle(ll2))


