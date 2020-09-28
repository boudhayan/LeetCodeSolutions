class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        while i < len(arr) - 1:
            if arr[i] != 0:
                i += 1
                continue
            k = i
            while k < len(arr) - 1:
                temp = arr[k+1]
                arr[k+1] = arr[i]
                arr[i] = temp
                k += 1
            arr[i] = 0
            i += 2
