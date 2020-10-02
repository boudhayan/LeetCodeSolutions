
# arr = [17, 18, 5, 4, 6, 1]

# l = len(arr) - 1
# for i in range(l, 0, -1):
#     if arr[i] > arr[i-1]:
#         arr[i-1] = arr[i]
#         print(arr)


# def moveZeros(arr):
#     zeroPos = len(arr)
#     temp = float("+inf")
#     for i in range(len(arr) - 1, -1, -1):
#         if arr[i] == 0:
#             zeroPos -= 1
#             k = i
#             while k < zeroPos:
#                 arr[k] = arr[k+1]
#                 k += 1
#             arr[zeroPos] = 0
#     print(arr)


# moveZeros([0, 1, 0, 3, 12])
