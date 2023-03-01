class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict_ = {}
        stack = []
        ans = []
        for n in nums2:
            while stack and n > stack[-1]:
                top = stack.pop()
                dict_[top] = n
            stack.append(n)

        for i in nums1:
            ans.append(dict_.get(i, -1))
        return ans