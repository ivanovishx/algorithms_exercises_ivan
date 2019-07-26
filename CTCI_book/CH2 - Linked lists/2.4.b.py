from LinkedList import LinkedList

def partition(l1, x):
	current = l1.tail == l1.head

	while current:
		nextNode = current.next
		current.next = None
		if current.value < x:
			current.next = l1.head
			l1.head = current
		else:
			l1.tail.next = current
			l1.tail = current
		current = nextNode

	# Error check in case all nodes are less than x
	if l1.tail.next is not None:
		l1.tail.next = None





list1 = LinkedList()
list1.generate(10,0,99)
print(list1)
partition(list1, list1.head.value)
print(list1)


ll = LinkedList()
ll.generate(10, 0, 99)
print(ll)
partition(ll, ll.head.value)
print(ll)