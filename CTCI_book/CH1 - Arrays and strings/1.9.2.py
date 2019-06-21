# 1.9 String Rotation: Assume you have a method  isSubstring which checks if one word 
# is a substring of another. Given two strings, S1 and S2, write code to check if S2 is a rotation of S1 
# using only one call to isSubstring (e.g., "waterbottle" is a rotation of u "erbottlewat").

#Runtime: O(N) because .find in isSubstring may last this time to find 
import unittest

def isSubstring(str1, sub):
	return str1.find(sub) != -1

def isRotation(S1, S2):	
	if len(S1) == len(S2) != 0:
		return isSubstring(S1+S1, S2)
	return False


class UnitTest(unittest.TestCase):

	data = [
		("waterbottle", "erbottlewat", True),
		("waterbottl", "erbottlewat", False),
		("waterbottle", "erbottlewa", False),
		("foo", "ofo", True),
		("foo", "off", False),
		("foo", "foo", True),
		("foo", "ffo", False),
		("","", False),
		("123", "321", False)
	 ]


	def test_code(self):
		for [s1, s2, expected] in self.data:
			value = isRotation(s1,s2)
			self.assertEqual(expected, value)


unittest.main()

# print(isRotation("waterbottle", "erbottlewat"))
# print(isRotation("waterbottl", "erbottlewat"))
# print(isRotation("waterbottle", "erbottlewa"))
# print(isRotation("foo", "ofo"))
# print(isRotation("foo", "off"))
# print(isRotation("foo", "foo"))
# print(isRotation("foo", "ffo"))
# print(isRotation("123", "321"))