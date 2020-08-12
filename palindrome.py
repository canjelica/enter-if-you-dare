"""Return True/False if this word is a palindrome. A palindrome is a word that is spelled the same backwards and forwards.

>>> is_palindrome("a")
True

>>> is_palindrome("noon")
True

>>> is_palindrome("racecar")
True

>>> is_palindrome("porcupine")
False
Treat spaces and uppercase letters normally—so “Racecar” wouldn’t be a palindrome since “R” and “r” aren’t the same letter:

>>> is_palindrome("Racecar")
False"""



def is_palindrome(word):
  """Return True/False if this word is a palindrome."""

	# reverse word, if word== word, true