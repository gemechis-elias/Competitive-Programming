class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        all_shifts = [0 for _ in range(len(s)+1)]
        
        for st, end, d in shifts:
            if d == 0:
                all_shifts[st] -= 1
                all_shifts[end+1] += 1
            else:
                all_shifts[st] += 1
                all_shifts[end+1] -= 1
        pr_sum = 0
        for i in range(len(s)):
            pr_sum += all_shifts[i]
            new_code = (((ord(s[i]) + pr_sum) - 97) % 26) + 97
            s = s[:i] + chr(new_code) + s[i+1:]
        
        
        return s
