class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        arr = [[scores[i], ages[i]] for i in range(len(scores))]
        arr.sort()
        if len(arr) == 1:
            return arr[0][0]
        ans = 0
        for i in range(1, len(scores)):
            maxi = 0
            summ = 0
            for j in range(i):
                if arr[j][1] <= arr[i][1]:
                    summ = arr[j][0] + arr[i][0]
                    maxi = max(summ, maxi)
            if maxi != 0:
                arr[i][0] = maxi
            ans = max(maxi, ans)

        return ans
