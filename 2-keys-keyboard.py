class Solution:
    def minSteps(self, n: int) -> int:
        prime_fact = []
        while n % 2 == 0:
            prime_fact.append(2)
            n = n / 2
        for i in range(3,int(math.sqrt(n))+1,2):
            while n % i== 0:
                prime_fact.append(i)
                n = n / i
        if n > 2:
            prime_fact.append(n)
        
        return int(sum(prime_fact))