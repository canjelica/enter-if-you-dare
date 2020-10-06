class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        elements = {}
        majority = len(nums) / 2
        
        for num in nums:
            if num in elements:
                elements[num] += 1
            else:
                elements[num] = 1
       
        
        for element in elements:
            if elements[element] > majority:
                return element


class Solution:
    def reformatDate(self, date: str) -> str:
        # break up by spaces
        # save each piece to variable
        # return date first
        #
        
        months = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04",                     "May":"05", "Jun": "06","Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}
        
        day, month, year = date.split()
        month = str(months[month])
        
        day = day[:-2]
        
        if len(day) == 1:
            day = "0" + day
        

        return year + "-" + month + "-" + day