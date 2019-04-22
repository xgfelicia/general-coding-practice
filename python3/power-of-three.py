class Solution:
    def __init__(self):
        self.max = 3 ** 1291

    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        return (self.max % n == 0)
