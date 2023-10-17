class SegmentTree:
    def __init__(self, n):
        self.tree = [0] * 4 * n
        self.n = n
    
    def update(self, l, r, x, val, treeIdx):
        if l == r - 1:
            self.tree[treeIdx] = max(self.tree[treeIdx], val)
            return 
        
        c = (l + r) // 2
        if x < c:
            self.update(l, c, x, val, 2 * treeIdx)
        else:
            self.update(c, r, x, val, 2 * treeIdx + 1)

        self.tree[treeIdx] = max(self.tree[2 * treeIdx], self.tree[2 * treeIdx + 1])
    
    def query(self, lDesired, rDesired, l, r, treeIdx):
        if lDesired <= l and rDesired >= r:
            return self.tree[treeIdx]
        
        c = (l + r) // 2
        leftMax, rightMax = 0, 0
        if lDesired < c:
            leftMax = self.query(lDesired, rDesired, l, c, 2 * treeIdx)
        if rDesired > c:
            rightMax = self.query(lDesired, rDesired, c, r, 2 * treeIdx + 1)
        
        return max(leftMax, rightMax) 
    
class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        n = max(nums)
        seg = SegmentTree(n)
        for num in nums:
            lis = seg.query(max(1, num - k), num, 1, n+1, 1)
            seg.update(1, n+1, num, lis+1, 1)

        #print(f'seg.tree = {seg.tree}')
        return seg.tree[1]