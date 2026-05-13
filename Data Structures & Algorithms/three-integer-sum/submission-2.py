class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results=[]
        for i in range(len(nums)-2): #for eaach i 
            if i>0 and nums[i] == nums[i-1]:
                continue
            left=i+1
            right =len(nums)-1
            
            while left < right: #for one fixed i 
                sums = nums[i] + nums[left] + nums[right]
                if sums == 0:
                    results.append([nums[i],nums[left],nums[right]])
                    left = left+1
                    right =right-1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                        
                    while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                elif sums < 0:
                    left = left + 1
                else:
                    right = right-1
                    
        return results

        
        