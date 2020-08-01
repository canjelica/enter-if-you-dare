"""Write a function which takes a list of numbers and returns the length of the longest continuous stretch of a single number. For example, on the input [1,7,7,3], the correct return is 2, because there are two 7's in a row.

Write a doctest for this"""


def longest_continuous(nums):
	count = 0
	highest = 0

	if nums:
		current = nums[0]
	else:
		return 0

	for num in nums:

		if num == current:
			count += 1

			if count > highest:
				highest = count

		if num != current:
			count = 1
			current = num

	return highest
