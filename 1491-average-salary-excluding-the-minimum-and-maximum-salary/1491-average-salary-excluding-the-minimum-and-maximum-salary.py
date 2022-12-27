class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        return mean(salary[1:-1]) 
        