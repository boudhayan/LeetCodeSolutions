class Solution:
    def countDigit(self, n):
        c = 0
        while n > 0:
            n = n//10
            c += 1
        return c

    def findNumbers(self, nums: List[int]) -> int:
        ed = 0
        for num in nums:
            dc = self.countDigit(num)
            if dc % 2 == 0:
                ed += 1
        return ed
