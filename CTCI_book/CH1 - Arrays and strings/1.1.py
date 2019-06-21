
# 1.1 Implement an algorithm to determine if a string has all unique characters 
# What if you can not use additional data structures?


string_test1 = "abcdefgh123456"
string_test2 = "Achuuy76224sdf"

def is_unique(word):
	char_array = []
	for char in word:
		if char in char_array:
			return False
		else:
			char_array.append(char)

	return True


#Start


print (is_unique(string_test1))
print (is_unique(string_test2))