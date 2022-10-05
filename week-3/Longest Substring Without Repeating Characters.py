class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length=0
        win=""
        for i in s:
            while i in win:
                win = win[1:]
            win+=i
            max_length = max(max_length, len(win))
        return max_length
