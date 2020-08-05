"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""

def group_anagrams(strs):
        
	output = []
	letters = {}
		
	for word in strs:
		sorted_word = list(word)
		sorted_word.sort()
		#realized could also be done with sorted(word) and then "".join(word)
		sorted_word = "".join(sorted_word)
		
		letters[sorted_word] = letters.get(sorted_word, []) + [word]
		# print(letters)
	
	return [l for l in letters.values()]

	
