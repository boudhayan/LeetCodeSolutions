class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
            current_sum = 0
            dict = {}
            max_len = 0
            for i in range(len(nums)):
                if nums[i] == 0:
                    nums[i] = -1
                else:
                    nums[i] = 1
            for i in range(len(nums)):
                current_sum = current_sum + nums[i]
                if current_sum == 0:
                    max_len = i + 1
                if current_sum in dict:
                    if max_len < i - dict[current_sum]:
                        max_len = i - dict[current_sum]
                else:
                    dict[current_sum] = i
            return max_len