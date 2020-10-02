
def combinationSum(candidates, target):
    combinations = []
    candidates.sort()

    def solve(index=0, current_sum=0, taken=list()):
        if current_sum == target:
            combinations.append(taken[:])
            return
        for i in range(index, len(candidates)):
            if current_sum + candidates[i] > target:
                break
            solve(i, current_sum + candidates[i], taken + [candidates[i]])
    solve()
    return combinations


print(combinationSum([2, 3, 6, 7], 7))
