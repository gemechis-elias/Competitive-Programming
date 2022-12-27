class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        n = len(salary)
        total = sum(salary[1:-1])
        avarage = total/(n-2.0)
        
        return avarage
        