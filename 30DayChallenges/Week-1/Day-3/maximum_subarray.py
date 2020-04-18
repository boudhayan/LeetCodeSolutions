
def max_subarray(nums):
    max_so_far = nums[0]
    curr_max = nums[0]
    for i in range(1, len(nums)):
        curr_max = max(nums[i], curr_max + nums[i])
        max_so_far = max(curr_max, max_so_far)
    return max_so_far

print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))