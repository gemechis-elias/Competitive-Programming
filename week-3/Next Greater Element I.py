class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
      output=[]
      n=len(nums2)
      next_g=[-1]*n
      stack=[]
      dic={}
      for i in range(n):
          if not stack or nums2[stack[-1]]>=nums2[i]:
               stack.append(i)
          else:
              while stack and nums2[stack[-1]] <= nums2[i]:
                  next_g[stack[-1]]=nums2[i]
                  stack.pop()
              stack.append(i)
      dic={}
      for j in range(n):
          dic[nums2[j]]=next_g[j]
      for k in nums1:
          output.append(dic[k])
      return output
