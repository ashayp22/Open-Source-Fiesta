def isPalindrome(string):
	if len(string) <= 1:
		return True
	elif string[0] == string[-1]:
		return isPalindrome(string[1:-1])
	return False
		

print(isPalindrome("abc"))
print(isPalindrome("aba"))
print(isPalindrome("abba"))
print(isPalindrome("abbac"))
print(isPalindrome("abbba"))