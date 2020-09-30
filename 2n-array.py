class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        sorted_list = []
        x_list = nums[:n]
        y_list = nums [n:]
        #[2,5,1] [3,4,7]

        for i in range(n):
            sorted_list.append(x_list[i])
            sorted_list.append(y_list[i])
        
        return sorted_list
                
        



				#-------------------
			


			class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        
        good = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                    if nums[i] == nums[j]:
                        good += 1    
                    
        return good
                    
         
            
def numIdenticalPairs(self, nums: List[int]) -> int:
	dic = {1:3, 2:1, 3:2, }
	m = 3
	for n in nums:
		if n in dic:
			dic[n]+=1   
			m = max(m, dic[n])
		else:
			dic[n] = 1
            
	fac = [1, 1, 2, 6]
	for n in range(2, m+1):
		fac.append(n*fac[n-1])

	count = 0
	for k in dic:
		if(dic[k]>=2):
			count+=(fac[dic[k]]/(fac[dic[k]-2]*fac[2]))
	return int(count)
          