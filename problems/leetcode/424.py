from collections import defaultdict

class Solution:
    
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) < 2:
            return len(s)

        freq_dict, l, r, max_s = defaultdict(int), 0, 1, 1
        freq_dict[s[l]] += 1
        while r < len(s):
            freq_dict[s[r]] += 1
            ss_len = r - l + 1
            max_c = max(freq_dict.values()) 
            if (ss_len - max_c) <= k:
                max_s = max(ss_len, max_s)
                r += 1
            else:
                freq_dict[s[l]] -= 1
                l += 1
                r += 1
    
        return max_s