# 1.2 (old)Write code to reverse a C-Style String 
# (C-String means that “abcd” is represented as five characters, including the null character )


# 1.2 (OK new) Given two strings write a method to decide if one is permutation of the other

def is_permutation(word1, word2):
	if len(word1) != len(word2):	
		return False
		
	for char in word1:
		if char not in word2:
			return False
	return True



def sort_compare(word1, word2):
	word1 = sorted(word1)
	word2 = sorted(word2)
	if word1 == word2:
		return True
	return False



# Start

word1 = "abcd"			
word2 = "cdba"
word3 = "aert"
word4 = "abcde"
word5 = "abbd"


print (is_permutation(word1, word2))
print (is_permutation(word1, word3))
print (is_permutation(word1, word4))
print (is_permutation(word1, word5))
print (is_permutation(word2, word1))
print("----Sorted----")
print (sort_compare(word1, word2))
print (sort_compare(word1, word3))
print (sort_compare(word1, word4))
print (sort_compare(word1, word5))
print (sort_compare(word2, word1))