class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        maxim = 1440

        for i, time in enumerate(timePoints):
            hh, mm = map(int, time.split(':'))
            timePoints[i] = (hh*60) + mm

        ans = inf
        timePoints.sort()
        print('a: ', timePoints)
        for i in range(len(timePoints)):
            if i-1 >= 0:
                ans = min(ans, abs(timePoints[i-1]-timePoints[i]))
            if i+1 < len(timePoints):
                ans = min(ans, abs(timePoints[i+1]-timePoints[i]))

        ans = min(ans, abs(abs(timePoints[0]-0)+abs(timePoints[-1]-maxim)))

        return ans