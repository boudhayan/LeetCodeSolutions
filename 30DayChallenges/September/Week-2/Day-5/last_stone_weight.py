class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        if len(stones) == 0:
            return 0
        stones.sort()
        first_stone = stones.pop(-1)
        second_stone = stones.pop(-1)
        if first_stone == second_stone:
            return self.lastStoneWeight(stones)
        else:
            remaining_weight = first_stone - second_stone
            stones.append(remaining_weight)
            return self.lastStoneWeight(stones)