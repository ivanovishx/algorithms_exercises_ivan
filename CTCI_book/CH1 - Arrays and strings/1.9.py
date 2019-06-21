# 1.9 String Rotation: Assume you have a method  isSubstring which checks if one word 
# is a substring of another. Given two strings, S1 and S2, write code to check if S2 is a rotation of S1 
# using only one call to isSubstring (e.g., "waterbottle" is a rotation of u "erbottlewat").


def isSubstring(str1, str2):
	return str1.find(str2) != -1

	

def isRotation(str1, str2):
	# startIndex = isSubstring(str1, str2)
	if len(str1) == len(str2):
		# print("-",str1+str1,"--")
		# print("Hi")
		return isSubstring(str1+str1, str2)
	return False


#Start
print (isRotation("waterbottle", "erbottlewat"))




a = "waterbottlewaterbottle"
print(a.find("F"))
print(a.find("f"))
print(a.find("n"))
print(a.find("ness"))
print(a.find("ess"))
print(a.find("z"))
print(a.find("Homer"))
print(a.find("erbottlewat"))
