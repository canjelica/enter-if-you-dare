"""Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        
        s = sorted(s)
        t = sorted(t)
        
        if s == t:
            return True
        else:
            return False



class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        shuffled = ""
        
        i=0
        while i < len(s):
            shuffled = shuffled + s[indices.index(i)]
            i+=1

        return shuffled
        
        
        
            
    
    
            
        
        