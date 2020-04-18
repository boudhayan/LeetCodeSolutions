
def moveZeroes(nums):
    nxt = 0
    for n in nums:
        if n != 0:
            nums[nxt] = n
            nxt += 1
    for j in range(nxt, len(nums)):
        nums[j] = 0
    return nums

print(moveZeroes([0,1,0,3,12]))       
