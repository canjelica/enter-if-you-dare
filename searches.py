"""Quicksort"""


def quicksort(nums):
	if len(nums) <= 1:
		return nums
	else:
		pivot = nums.pop()
	
	greater_than = []
	less_than = []

	for num in nums:
		if num < pivot:
			less_than.append(item)
		if num > pivot:
			greater_than.append(item)
	
	return quicksort(less_than) + [pivot] + quicksort(greater_than)



def quicksort_alt(lst):

    # if length of lst is 1, return lst
    if len(lst) < 2:
        return lst

    # select pivot element
    mid = int(len(lst) / 2)  # index at half the list
    pivot = lst[mid]

    # partition elements into lo , hi , eq buckets
    lo , hi , eq = [] , [] , []
    for elem in lst :
        if elem < pivot :
            lo.append(elem)
        elif elem == pivot :
            eq.append(elem)
        else :  #  elem > pivot
            hi.append(elem)

    # concatenate sorted buckets and finish
    return quicksort(lo) + eq + quicksort(hi) #lists added together equal one big list, eq is already a list vs in the first version where you make it  a list

"""Mergesort"""

def merge_sort(lst):
    """Merge sort list and return result."""

    print("calling merge_sort on", lst)

    # Break everything down into a list of one
    if len(lst) < 2:  # if length of lst is 1, return lst
        print("returning", lst)
        return lst

    mid = int(len(lst) / 2)  # index at half the list
    lst1 = merge_sort(lst[:mid])  # divide list in half
    lst2 = merge_sort(lst[mid:])  # assign other half

    return make_merge(lst1, lst2)


def make_merge(lst1, lst2):
    """Merge lists."""

    # Compare first items of each pair of lists & interleave
    result_list = []
    print(lst1, lst2)
    while len(lst1) > 0 or len(lst2) > 0:
        # if items left in both lists
        # compare first items of each list
        if lst1 == []:
            result_list.append(lst2.pop(0))
        elif lst2 == []:
            result_list.append(lst1.pop(0))
        elif lst1[0] < lst2[0]:
            # append and rm first item of lst1
            result_list.append(lst1.pop(0))
        else:
            # append and rm first item of lst2
            result_list.append(lst2.pop(0))

    print("returning merge", result_list)
    return result_list



"""Binary Search"""

def binary_search(sequence, item):
    begin_index = 0
    end_index = len(sequence) - 1

    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_value = sequence[midpoint]
        if midpoint_value == item:
            return midpoint

        elif item < midpoint_value:
            end_index = midpoint - 1

        else:
            begin_index = midpoint + 1

    return None

sequence_a = [2,4,5,6,7,8,9,10,12,13,14]
item_a = 2


print(binary_search(sequence_a, item_a))



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
