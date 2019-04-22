class Solution:
    def countPrimes(self, n: int) -> int:
        total = 0
        prime = [False, False] + [True] * (n-2)

        for i in range(2, n):
            if prime[i]:
                for j in range(i*2, n, i):
                    prime[j] = False


        return sum(prime)
            
