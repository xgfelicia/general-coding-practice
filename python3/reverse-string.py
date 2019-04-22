class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start = 0
        end = len(s) - 1

        if start < end:
            for i in range(int(end/2)+1):
                s[end], s[start] = s[start], s[end]
                start += 1
                end -= 1
