class Solution:
    def countElements(self, arr: List[int]) -> int:
        x = 0
        for num in arr:
            f = num + 1
            if f in arr:
                x += 1
        return x