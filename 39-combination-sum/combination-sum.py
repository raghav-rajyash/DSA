class Solution:
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(start, target, path):
            # Base case
            if target == 0:
                result.append(path[:])
                return
            
            if target < 0:
                return
            
            for i in range(start, len(candidates)):
                # choose
                path.append(candidates[i])
                
                # explore (same i → reuse allowed)
                backtrack(i, target - candidates[i], path)
                
                # undo (backtrack)
                path.pop()

        backtrack(0, target, [])
        return result