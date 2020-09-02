"""

Output Format

Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than a 32 bit integer.)

Sample Input

1 2 3 4 5
Sample Output

10 14
Explanation

The numbers are , , , , and . Calculate the following sums using four of the five integers:

Sum everything except , the sum is .
Sum everything except , the sum is .
Sum everything except , the sum is .
Sum everything except , the sum is .
Sum everything except , the sum is .
Hints: Beware of integer overflow! Use 64-bit Integer.
"""


# def mini_max(nums):

	# #sort list 
	# #add the ints from index 0 to index -2 to get min
	# #add the ints from index 1 to index -1 to get max
	# # print min max
	# def quicksort(nums):
	# 	if len(nums) <= 1:
	# 		return nums
	# 	else:
	# 		pivot = nums.pop()
		
	# 	items_greater = []
	# 	items_lower = []

	# 	for item in nums:
	# 		if item > pivot:
	# 			items_greater.append(item)
	# 		else item < pivot:
	# 			items_lower.append(item)
	# 	nums =  quicksort(items_lower) + [pivot] + quicksort(items_lower)
	
	# i = 0
	# min = 0
	# max = 0
	# while i < len(nums)-1:
	# 	min += nums[i] 
	# 	i += 1
	



def miniMaxSum(arr):
    biggest = max(arr)
    smallest = min(arr)
    total = 0

    for num in arr:
        total += num
    
    maximum_sum = total - smallest
    minimum_sum = total - biggest

    print(minimum_sum, maximum_sum)