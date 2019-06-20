# Write a method to replace all spaces in a string with ‘%20’


def replace_spaces(str):
	new_str = ""
	for char in str:
		if char == " ":
			# new_str.append("%20")
			new_str += "%20"
		else:
			# new_str.append(char)
			new_str += char
	return new_str


#Start


sample = "Ivan Lozano is cool and ?"

print(sample)	
print(replace_spaces(sample))