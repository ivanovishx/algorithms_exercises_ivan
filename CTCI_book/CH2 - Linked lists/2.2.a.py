# 2.2- Return Kth to Last: Implement an algorithm to find the Kth 
# to last element of a single linked list.
#Recursive way   NEEDS TO BE IMPROVED!!!!

class Node():
	def __init__(self, data, next):
		self.data = data
		self.next = next

def returnK(head, k):
	if not head:
		return 0

	list_len = returnK(head.next, k) + 1
	if (list_len == k):
		print(k, "from last is:", head.data)
	return list_len

	'''while node:
					list_len += 1
					print("while", list_len)
					if node.next: 
						node = node.next
					else:
						# list_len += 1
						# print(list_len)
						break
			
			
				for i in range(list_len):
					print("for", node.data)
					head = node.next
			
			
			
				return node
	'''

#Start
ll1 = Node(1,Node(2,Node(3,Node(4,Node(5,Node(6,Node(7,None)))))))

print(returnK(ll1,0))
print(returnK(ll1,1))
print(returnK(ll1,2))
print(returnK(ll1,6))