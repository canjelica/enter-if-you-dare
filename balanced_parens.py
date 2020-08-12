"""Given a string, return True if the string has balanced parentheses.

For example:

>>> has_balanced_parens('()')
True
 
>>> has_balanced_parens('((Oh no!)')
False"""

#use a stack for matching problems
#loop over each character in string
#if encounter a "(", add to stack
#if a ")" try to pop, if there's nothing to pop return false because the parens are unbalanced
# if the loop completes, return True if stack len is 0

def is_balanced(sentence):
	"""Return True is parens are balanced."""

	parens_stack = []

	for char in sentence:
		if char == "(":
			parens_stack.append(char)
		if char == ")":
			try:
				parens_stack.pop()
			except IndexError:
					return False
	if len(parens_stack) == 0:
		return True
	# return len(parens_stack) == 0
	#^^^ len returns a number, if not equal to 0 will be False


	#----------NO STACK----------------#


def f(ch, count):
    if ch == '(':
        return count + 1
    elif ch == ')':
        return count - 1
    else:
        return count

def has_balanced_parens(phrase):
    parens = 0

    for char in phrase:
        parens = f(char, parens)
            
        if parens < 0:
            return False

    return parens == 0