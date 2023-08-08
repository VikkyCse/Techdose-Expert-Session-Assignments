#1755. Closest Subsequence Sum
class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        def dfs(nums, i, s):
            if i == len(nums):
                return [s]
            return dfs(nums, i + 1, s) + dfs(nums, i + 1, s + nums[i])
        n = len(nums)
        left = dfs(nums[:n // 2], 0, 0)
        right = dfs(nums[n // 2:], 0, 0)
        left.sort()
        right.sort()
        ans = float('inf')
        j = len(right) - 1
        for x in left:
            while j >= 0 and x + right[j] > goal:
                j -= 1
            if j >= 0:
                ans = min(ans, abs(x + right[j] - goal))
            if j + 1 < len(right):
                ans = min(ans, abs(x + right[j + 1] - goal))
        return ans

