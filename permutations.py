class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(bitmask, current):
            if bitmask == (1 << len(nums)) - 1:
                permutations.append(current[:])
            else:
                for i in range(len(nums)):
                    if not bitmask & (1 << i):
                        bitmask |= (1 << i)
                        current.append(nums[i])
                        backtrack(bitmask, current)
                        bitmask &= ~(1 << i)
                        current.pop()

        permutations = []
        backtrack(0, [])
        return permutations