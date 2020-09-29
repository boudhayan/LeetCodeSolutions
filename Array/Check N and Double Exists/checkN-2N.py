class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        dict = {}
        for num in arr:
            d = 2 * num
            h = float("+inf")
            if num % 2 == 0:
                h = num // 2
            if (d in dict) or (h in dict):
                return True
            else:
                dict[num] = True
        return False
