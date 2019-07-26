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

# Solution from 
# https://github.com/w-hat/ctci-solutions/blob/master/ch-02-linked-lists/04-partition.py





# Partition a linked list so that all of the nodes containing values less than
# a pivot value occur before all of the nodes containing values greater than
# or equal to the pivot value.

import unittest

def partitionNode(head, pivot):
  a_head, a_tail = None, None
  b_head, b_tail = None, None
  node = head
  while node:
    if node.data < pivot:
      if a_head:
        a_tail.next, a_tail = node, node
      else:
        a_head, a_tail = node, node
    else:
      if b_head:
        b_tail.next, b_tail = node, node
      else:
        b_head, b_tail = node, node
    node = node.next
  a_tail.next = b_head
  return a_head

class Node():
  def __init__(self, data, next=None):
    self.data, self.next = data, next
  
  def __str__(self):
    string = str(self.data)
    if self.next:
      string += ',' + str(self.next)
    return string

def printList(head):
	if head.next:
		print(head.data)
		printList(head.next)

# class Test(unittest.TestCase):
  # def test_partition(self):
    # head1 = Node(7,Node(2,Node(9,Node(1,Node(6,Node(3,Node(8)))))))
    # head2 = partition(head1, 6)
    # self.assertEqual(str(head2), "3,5,8,5,10,2,1") 
    # 3 -> 5 -> 8 ->  5 -> 10 -> 2 -> 1
    # head3 = partition(head2, 7)
    # self.assertEqual(str(head3), "2,1,3,6,7,9,8")

# if __name__ == "__main__":
  # unittest.main()

list1 = Node(3,Node(5,Node(8,Node(5,Node(10,Node(2,Node(1)))))))# expected Output: 	3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
list2 = partitionNode(list1, 5)
printList(str(list2))

# head1 = Node(7,Node(2,Node(9,Node(1,Node(6,Node(3,Node(8)))))))
# head2 = partition(head1, 6)
# print(str(head2), "2,1,3,7,9,6,8")


