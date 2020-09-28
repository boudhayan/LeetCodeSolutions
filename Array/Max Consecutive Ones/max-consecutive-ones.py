class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        isOnes = False
        cm = 0
        ones = 0
        for num in nums:
            if num == 1:
                isOnes = True
            else:
                isOnes = False
                cm = 0
                continue
            if isOnes:
                cm += 1
            if cm > ones:
                ones = cm
        return ones
