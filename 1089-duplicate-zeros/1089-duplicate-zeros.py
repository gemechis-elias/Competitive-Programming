class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        index = 0
        while index < len(arr):
            if arr[index] == 0:
                arr.insert(index + 1, 0)
                arr.pop()
                index += 1
            index += 1
        return arr