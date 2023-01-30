class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        rightmost = {c:i for i, c in enumerate(s)}
        left, right = 0, 0
        result = []
        for i, letter in enumerate(s):
            right = max(right, rightmost[letter])
            if i == right:
                result += [right-left + 1]
                left = i+1

        return result
