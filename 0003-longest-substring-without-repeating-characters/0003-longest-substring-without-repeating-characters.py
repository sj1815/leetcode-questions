class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left = 0
        set_of_chars = set()
        longest = 0

        for right in range(n):
            while s[right] in set_of_chars:
                set_of_chars.remove(s[left])
                left += 1
            
            w = (right - left) + 1
            longest = max(longest, w)
            set_of_chars.add(s[right])
        
        return longest