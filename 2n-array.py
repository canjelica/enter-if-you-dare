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
                
        