"""Return the date on second week of October in a Gregorian calendar"""


"""Calculating whether a value is greater than the average value of consecutive subsets of data of certain window size."""

"""find the average of subsets of window size, if value is greater return whatever

Given an array and an integer K, find the maximum for each and every contiguous subarray of size k.
Examples :

Input: arr[] = {1, 2, 3, 1, 4, 5, 2, 3, 6}, K = 3 
Output: 3 3 4 5 5 5 6
Explanation: 
Maximum of 1, 2, 3 is 3
Maximum of 2, 3, 1 is 3
Maximum of 3, 1, 4 is 4
Maximum of 1, 4, 5 is 5
Maximum of 4, 5, 2 is 5 
Maximum of 5, 2, 3 is 5
Maximum of 2, 3, 6 is 6

Input: arr[] = {8, 5, 10, 7, 9, 4, 15, 12, 90, 13}, K = 4 
Output: 10 10 10 15 15 90 90
Explanation:
Maximum of first 4 elements is 10, similarly for next 4 
elements (i.e from index 1 to 4) is 10, So the sequence 
generated is 10 10 10 15 15 90 90


https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/
"""

#loop over the array in chunks of 3
#find max each time, add to new array
#set i to 0, slice from i until end 
#account for index error at end

# def find_max_window(array, k):
# 	output = []

# 	i = 0

# 	for i, window in array:


def make_everything_a_list_of_one(lst):
    """Divide lists until we reach lists of length 1."""

    # if length of lst is 1, return lst
    if len(lst) < 2:
        print(lst)
        return lst

    # index at half the list
    mid = int(len(lst) / 2)

    # divide list in half
    make_everything_a_list_of_one(lst[:mid])
    # assign other half
    make_everything_a_list_of_one(lst[mid:])


lst2 = [2, 1, 7, 4]
make_everything_a_list_of_one(lst2)      # => [2] [1] [7] [4]