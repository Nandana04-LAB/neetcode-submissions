class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        freq = {}
        max_len = 0
        for i in range (len(s)):
            freq[s[i]] = freq.get(s[i], 0) + 1
            max_freq = max(freq.values())
            current_window_size  = i-left+1
            replacement  = current_window_size - max_freq

            if replacement > k :
                freq[s[left]] = freq[s[left]] - 1
                left = left+1
                current_window_size  = i-left+1
            if max_len < current_window_size :
                max_len = current_window_size

        return max_len
            
            

            
