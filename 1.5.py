#1.5 One Away: There are three types of edits that can be performed on strings: 
# insert a character, remove a character, or replace a character. Given two strings, 
# write a function to check if they are one edit (or zero edits) away.

# EXAMPLE
# pale, ple -> true 
# pales, pale -> true 
# pale, bale -> true 
# pale, bae -> false


import unittest


def changeAway(str1, str2):
	# count_edits = 0
	# max_edits = 1

	#find replace
	if len(str1) == len(str2):
		return countReplaces(str1, str2)
	#find Insert
	elif len(str1) + 1 == len(str2):
		return countInserts(str1, str2)
	#find remove
	elif len(str1) - 1 == len(str2):
		return countRemoves(str1, str2)
	else:
		return False

	# print("In {} :: {} |We need to edit: {}" .format(str1, str2, count_edits) )
	
	# if count_edits > 1:
		# return False
	# return True	

		
def countReplaces(str1, str2):
	edited = False
	for i in range(len(str1)):
		if str1[i] != str2[i]:
			if edited:
				return False
			edited = True
	return True	

# def countReplacesZipWay(str1, str2):
# 	edited = False
# 	for char1,char2 in zip(str1,str2):
# 		if char1 != char2:
# 			if edited:
# 				return False
# 			edited = True
# 	return True	



def countInserts(str1, str2):
	edited = False
	i, j = 0, 0
	while i < len(str1) and j < len(str2):
		if str1[i] != str2[j]:
			if edited:
				return False
			edited = True
			j += 1
		else:			
			i += 1
			j += 1
	return  True


def countRemoves(str1, str2):
	return countInserts(str2, str1)


#Unit testing:
class Test(unittest.TestCase):


	data = [
		('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False),
        ('abc', 'accd', False)
	]

	def test_one_way(self):
		for [str1, str2, expected] in self.data:
			actual = changeAway(str1, str2)
			self.assertEqual(actual, expected)


#Start
# print(changeAway("pale", "ple"))
# print(changeAway("pale", "palec"))
# print(changeAway("pales", "pale"))
# print(changeAway("pale", "bale"))
# print(changeAway("pale", "bae"))
# print(changeAway("abc", "accd"))

#Start unit testing:

if __name__ == "__main__":
	unittest.main()
