
def merge(nums1, m, nums2, n):
    i = m - 1
    j = n - 1
    x = m + n - 1
    while i > -1 and j > -1:
        if nums1[i] > nums2[j]:
            nums1[x] = nums1[i]
            x -= 1
            i -= 1
        elif nums1[i] < nums2[j]:
            nums1[x] = nums2[j]
            j -= 1
            x -= 1
        else:
            nums1[x] = nums1[i]
            x -= 1
            i -= 1
            nums1[x] = nums2[j]
            x -= 1
            j -= 1
    while j > -1:
        nums1[x] = nums2[j]
        j -= 1
        x -= 1


merge([1, 2, 3, 0, 0, 0], 3,  [4, 5, 6], 3)
# [4, 5, 6, 0, 0, 0]  [1, 2, 3]
# i = 2, j = 2
