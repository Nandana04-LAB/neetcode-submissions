class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        min_diff = float('inf')

        for i in range(len(nums)-k+1):
            diff = nums[i+k-1] - nums[i]
            if min_diff>diff:
                min_diff=diff
        return min_diff
            