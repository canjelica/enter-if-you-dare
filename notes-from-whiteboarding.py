"""
In order to win the prize for most cookies sold, my friend Alice and I are going to merge our Girl Scout Cookies orders and enter as one unit.

Each order is represented by an "order id" (an integer).

We have our lists of orders sorted numerically already, in lists. 

Write a function to merge our lists of orders into one sorted list.

For example:  my_list     = [3, 4, 6, 10, 11, 15]

alices_list = [1, 5, 8, 12, 14, 19]

# Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19] print(merge_lists(my_list, alices_list)) """



"""Initialize new, empty list for results
Compare first element of each sorted list
Figure out which element is lower and add it to the results list
Continue comparing 1st elements of each list until you finish one list
Append the remaining items from the other, unfinished list to results list"""

def merge_lists(list1, list2):
	"""Merges two already-sorted lists."""

	merged_list = []

	while len(list1) > 0 or len(list2) > 0:
		if list2 == []:  #if not list2
			merged_list.append(list1.pop(0))
		elif list1 == []:
			merged_list.append(list2.pop(0))
		elif list1[0] < list2[0]:
			smaller = list1.pop(0)
			merged_list.append(smaller)
		elif list2[0] < list1[0]:
			smaller = list2.pop(0)
			merged_list.append(smaller)
		else:  
			merged_list.append(list1.pop(0))
			merged_list.append(list2.pop(0))
	
	return merged_list #to catch else, + list1 + list 2

	merge_lists([19], [])

	[1,3,4,5,6,8,10,11,12,14,15]

def test_both_lists_are_empty(self):
	actual = merge_lists([], [])
	expected = []
	self.assertEqual(actual, expected)
		
def test_first_list_is_empty(self):
	actual = merge_lists([], [1, 2, 3])
	expected = [1, 2, 3]
	self.assertEqual(actual, expected)

def test_second_list_is_empty(self):
	ctual = merge_lists([5, 6, 7], [])
	expected = [5, 6, 7]
	self.assertEqual(actual, expected)

def test_both_lists_have_some_numbers(self):
	actual = merge_lists([2, 4, 6], [1, 3, 7])
	expected = [1, 2, 3, 4, 6, 7]
	self.assertEqual(actual, expected)

def test_lists_are_different_lengths(self):
	actual = merge_lists([2, 4, 6, 8], [1, 7])
	expected = [1, 2, 4, 6, 7, 8]
	self.assertEqual(actual, expected) 