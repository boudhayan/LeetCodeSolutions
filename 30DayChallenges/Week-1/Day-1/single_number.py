
class Solution:
    def singleNumber(self, nums): 
        num = nums[0]
        for i in range(1, len(nums)):
            num = num ^ nums[i]
        return num


sol = Solution()
print(sol.singleNumber([4,1,2,1,2]))