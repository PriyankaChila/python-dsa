from typing import List

from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # num_list = sorted(nums)
        index=0
        start_position = 0
        end_position = 0
        start_counter = False
        for i in range(index, len(nums)):
            if nums[i] == target:
                start_position = i
                print(start_position)
                break
        reverse_num = nums[::-1]
        for i in range(index, len(reverse_num)):
            if reverse_num[i] == target:
                end_position = len(reverse_num)-(i+1)
                break
        
        
        return start_position, end_position


nums =[5,7,7,8,8,10]

target = 8
obj = Solution()
print(type(obj.searchRange(nums, target)))
        
        
            
                
                
                
                

        
        
            
                
                
                
                
