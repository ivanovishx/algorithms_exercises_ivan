#1.4 Given a string, write a function to check if it is a permutation of a palin- drome.
# A palindrome is a word or phrase that is the same forwards and backwards. 
# A permutation is a rearrangement of letters.The palindrome does not need to be limited to just dictionary words.


def isPalondrome(str1, str2):
	if len(str1) != len(str2):
		return False

	char_odd_count = 0
	if len(str1)%2 > 0: #is odd
		countEvens = int(len(str1))
		str1 = sorted(str1)
		for char in range(len(str1)): 
			print ("char:", str1[char], str1[char+1], char)
			
			

			if str1[char + char_odd_count] != str1[char+1  + char_odd_count]:
				char_odd_count += 1
				char += 1

			# if (char_odd_count > 1):
				# return False

		return True


	else: #is even
		return True


def isPalondromeMap(str1, str2):
	mapStr1 = {}
	count_odd = 0
	for char in str1:
		mapStr1[char] = 0

	for char in str1:	
		mapStr1[char] += 1
		if mapStr1[char] > 2:
			print (mapStr1)
			return False

	for char in str1:
		if mapStr1[char] == 1:
			count_odd += 1
			if count_odd > 1:
				print (mapStr1)
				return False

	print (mapStr1)
	return True





	

	# for char in str1:
	# 	if mapStr1[char] == 1: #Check for more than one odd number
	# 		if count_odd:
	# 			print (mapStr1)
	# 			return False
	# 		count_odd = True
			

	print (mapStr1)
	return True	



#Start


# print(isPalondrome("holahola1", "oalh1halo"))
print(isPalondromeMap("holahola111", "oalh1halo"))
print(isPalondromeMap("oalh1halo", "oalh1halo"))
print(isPalondromeMap("hola2hola1", "oalh1halo"))


