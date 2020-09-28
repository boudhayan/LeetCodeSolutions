
def removeElement(nums, val):
    i = 0
    while i < len(nums):
        if nums[i] == val:
            del nums[i]
        i += 1
    return len(nums)


print(removeElement([1, 2, 3], 2))
