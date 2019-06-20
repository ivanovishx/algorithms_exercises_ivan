# 1.6 String Compression: Implement a method to perform basic string 
# compression using the counts of repeated characters. 
# For example, the string aabcccccaaa would become a2b1c5a3. 
# If the "compressed"string would not become smaller than the 
# original string, your method should return the original string. 
# You can assume the string has only uppercase and lowercase letters (a - z).


import unittest

def compress(str1):
	str2 = ""
	previus_char = ''
	count = 0
	for i in range(len(str1)):		
		if previus_char == str1[i]:
			count += 1
		else:
			previus_char = str1[i]
			str2 += str(count) + str1[i] 
			if count == 0:
				count +=1
			else:
				count = 0	
		if len(str2) > len(str1):
				return str1			
	str2 += str(count)

	if len(str2) > len(str1):
		return str1
	else:
		return str2

def compress_v2(str1):
	str2 = ""
	previus_char = ""
	count = 0

	for i in range(len(str1)):
		if previus_char != str1[i]:
			if previus_char != "":
				str2 += str(count)
			str2 += str1[i]
			count = 1
			previus_char = str1[i]
		else:
			count += 1

	str2 += str(count)	
	if len(str1) > len(str2):
		return 	str2
	else:
		return str1


def string_compression(string):
	compressed = []
	counter = 0

	for i in range(len(string)):
		if i != 0 and string[i] != string[i - 1]:
			compressed.append(string[i - 1] + str(counter))
			counter = 0
		counter += 1
	compressed.append(string[-1] + str(counter))

	return min(string, ''.join(compressed), key=len)



#Unit testing

class Test(unittest.TestCase):

	data = [
		("aabcccccaaa","a2b1c5a3"),
		("aabccccca","a2b1c5a1"),
		("abcd","abcd"),
		("abbbb","a1b4"),
	]

	def testCompress(self):
		for [data_string, expected] in self.data:
			evaluate = compress_v2(data_string)
			self.assertEqual(evaluate, expected)




#Start
print(compress_v2("aabcccccaaa"))
print(compress_v2("aabccccca"))
print(compress_v2("abcd"))
print(compress_v2("abbbb"))
# aabcccccaaa  a2b1c5a3

unittest.main()
