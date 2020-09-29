
def validMountainArray(arr):
    if len(arr) < 3:
        return False
    i = 1
    while i < len(arr) - 1:
        if arr[i-1] < arr[i] and arr[i] > arr[i+1]:
            return checkMountain(i, arr, arr[i])
        i += 1
    return False


def checkMountain(i, arr, top):
    j = i - 2
    k = i + 2
    while j >= 0:
        if arr[j] >= arr[j+1]:
            return False
        j -= 1
    while k < len(arr):
        if arr[k-1] <= arr[k]:
            return False
        k += 1
    return True


print(validMountainArray([0, 3, 2, 1]))
