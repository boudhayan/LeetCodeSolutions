
arr = [[1, 2, 3], [4, 5], [1, 2, 3]]


def maxDistance(arrays):
    distance = 0
    cMin = arrays[0][0]
    cMax = arrays[0][len(arrays[0] - 1)]
    for i in range(1, len(arrays)):
        array = arrays[i]
        cDis1 = abs(cMin - array[len(array - 1)])
        cDis2 = abs(cMax - array[0])
        distance = max(distance, cDis1, cDis2)
        cMin = min(cMin, array[0])
        cMax = max(cMax, array[len(array) - 1])
    return distance


print(maxDistance(arr))
