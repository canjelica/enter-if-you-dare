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

	