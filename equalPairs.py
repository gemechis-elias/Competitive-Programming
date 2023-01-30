class Solution(object):
    def equalPairs(self, grid):
        number = len(grid)
        answer = 0
        
        for row in range(number):
            for col in range(number):
                found = True
                for index in range(number):
                    if grid[row][index] != grid[index][col]:
                        found = False
                        break
                if found:
                    answer += 1
					
        return answer
