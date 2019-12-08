#!/usr/bin/python3

print("\n",
      '   Ask the user for a string and print out whether this string is a palindrome or not.',
      "\n",
      '   PS: A palindrome is a string that reads the same forwards and backwards.'
      "\n",
      "-------------------------------------------------------------------------------------------------------")

def reverse(word):
	x = ''
	for i in range(len(word)):
		x += word[len(word)-1-i]
		return x

if __name__ == "__main__":
    word = input('give me a word:\n')
    x = reverse(word)
    if x == word:
        print('This is a Palindrome')
    else:
	    print('This is NOT a Palindrome')
