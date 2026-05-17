class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0
        min_len = float('inf')

        for i in range(len(nums)):
            total = total + nums[i]

            while total >= target:

                current_len = i-left +1
                if current_len < min_len:
                    min_len = current_len 
                total  = total - nums[left]
                left =left+1
        if min_len == float('inf'):
            return 0
        return min_len
                

       