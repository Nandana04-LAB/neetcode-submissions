class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        a = set()
        max_len= 0

        for i in range(len(s)):
            while s[i] in a:
                a.remove(s[left])
                left=left+1
            a.add(s[i])
            current_window = i - left+1
            if max_len < current_window:
                max_len = current_window 
                
        return max_len


