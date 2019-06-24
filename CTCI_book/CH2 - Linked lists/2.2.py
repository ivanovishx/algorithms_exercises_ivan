# 2.2- Return Kth to Last: Implement an algorithm to find the kth 
# to last element of a singly linked list.

import unittest

#Define Node Class		
class Node():
  def __init__(self, data, next):
    self.data = data
    self.next = next

 # IVAN SOlution #returns kth from the beggining to End
def returnSlideEnd(head, k): 
	count = 0
	while head.next != None:
		if count < k:
			count += 1
			head = head.next
		else:
			break
	return head


#Solution link  (this returns kth from last to k)
def returnSlideEnd2(head, k):
	lead, follow = head, head
	for i in range(k):
		print(i)
		if not lead:
			return None
		lead = lead.next
	while lead:
		lead, follow = lead.next, follow.next
	return follow



def printList(head):
	if head != None:
		print (head.data)
		printList(head.next)


linked_list = Node(1, Node(2,Node(3,Node(5,Node(6,Node(4,Node(4,Node(3,Node(4,None)))))))))
linked_list_2 = Node(1, Node(2,Node(3,Node(5,Node(6,Node(4,Node(4,Node(3,Node(4,None)))))))))
printList(linked_list)

linked_list = returnSlideEnd(linked_list, 1)
# print(returnSlideEnd(linked_list, 4))
print("-" * 10)
printList(linked_list)

#2:
print("2-" * 10)
printList(linked_list_2)
linked_list_2 = returnSlideEnd2(linked_list_2, 1)
print("-" * 10)
printList(linked_list_2)


