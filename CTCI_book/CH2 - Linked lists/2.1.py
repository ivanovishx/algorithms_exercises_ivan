# 2.1 Remove Dups: Write code to remove duplicates from an unsorted linked list. FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?

import unittest 
# O(N) time and O(N) space
def removeDuplicated(head):

	node = head

	if node:
		values = {node.data: True }

		while node.next:
			if node.next.data in values:
				node.next = node.next.next
			else:
				values[node.next.data] = True
				node = node.next

	return head
	# while(list.data != null):


class Node():
  def __init__(self, data, next):
    self.data = data
    self.next = next



class Test(unittest.TestCase):

	def test_remove_dup(self):
		head = Node(1,Node(3,Node(3,Node(1,Node(5,None)))))

		removeDuplicated(head)
		self.assertEqual(head.data, 1)
		self.assertEqual(head.next.data, 3)
		self.assertEqual(head.next.next.data, 5)


unittest.main()
