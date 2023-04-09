class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = [True] * (right+1)
        primes[0] = primes[1] = False
        for i in range(2, int(math.sqrt(right))+1):
            if primes[i]:
                for j in range(i*i, right+1, i):
                    primes[j] = False
        
        
        min_diff = float('inf')
        ans = []
        prev_prime = -1
        for i in range(left, right+1):
            if primes[i]:
                if prev_prime != -1:
                    diff = i - prev_prime
                    if diff < min_diff:
                        min_diff = diff
                        ans = [prev_prime, i]
                prev_prime = i
        
        return ans if ans != [] else [-1,-1]