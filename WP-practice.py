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



# Python program to find the maximum for  
# each and every contiguous subarray of 
# size k 
  
# Method to find the maximum for each 
# and every contiguous subarray of s  
# of size k 
def printMax(arr, n, k): 
    max = 0
    
    for i in range(n - k + 1): 
        max = arr[i] 
        for j in range(1, k): 
            if arr[i + j] > max: 
                max = arr[i + j] 
        print(str(max) + " ", end = "") 





class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsofar = nums[0]
        sumsofar = nums[0]
        for i in range(1, len(nums)):
            if sumsofar <= 0:
                sumsofar = nums[i]
            else:
                sumsofar =  sumsofar + nums[i]
                maxsofar = max(sumsofar, maxsofar)
        return maxsofar


class Sample:
	def __init__(self):
		self.a = 1;
		self.b = 1;
	
	def function_one(self,a):
		self.b = self.b + a
	
	def function_two(self, b):
		for i in range (self.b):
			self.a += b



def func(a):
	if a <= 0:
		return 1
	if a % 2 == 0:
		return a;
	else:
		return func(a-1) + func(a-2)


def hi(lst):                     

	a=0                                                  

	idx=0                                                

	while a<10: 
		if lst[idx] %2 == 0:
			a+= lst[idx]
			idx +=1
	print(str(a) + "," + str(idx))


heap sort
bogo sort
insertion
