def countSmaller(self, nums):
    def sort(indexes):
        half = len(indexes) / 2
        if half:
            left, right = sort(indexes[:half]), sort(indexes[half:])
            for i in range(len(indexes))[::-1]:
                if not right or left and nums[left[-1]] > nums[right[-1]]:
                    smaller[left[-1]] += len(right)
                    indexes[i] = left.pop()
                else:
                    indexes[i] = right.pop()
        return indexes
    smaller = [0] * len(nums)
    sort(range(len(nums)))
    return smaller
