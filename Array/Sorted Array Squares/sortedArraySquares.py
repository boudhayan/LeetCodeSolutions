class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        squares = [x*x for x in A]
        return sorted(squares)
