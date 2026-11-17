class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        left = 0
        count = {}
        max_len = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1

            while len(count) > 2:
                count[s[left]] -= 1

                if count[s[left]] == 0:
                    del count[s[left]]

                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len