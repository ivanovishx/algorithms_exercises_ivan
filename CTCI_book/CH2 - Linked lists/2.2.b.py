# 2.2- Return Kth to Last: Implement an algorithm to find the Kth 
# to last element of a single linked list.
#Iteractive way



class Node():
	def __init__(self, data, next):
		self.data = data
		self.next = next

def returnK(head, k):
	p1, p2 = head, head

	for i in range(k):
		if p1 == None:
			return None  #the list doesnt have enought positions (< K)
		p1 = p1.next

	while p1 != None:
		p1 = p1.next
		p2 = p2.next
	return p2


def printList(head):
	if head != None:
		print (head.data)
		printList(head.next)




#Start
ll1 = Node(1,Node(2,Node(3,Node(4,Node(5,Node(6,Node(7,None)))))))

# printList(returnK(ll1,0))
# printList(returnK(ll1,1))
printList(returnK(ll1,2))
# printList(returnK(ll1,6))