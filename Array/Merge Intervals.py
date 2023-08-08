#56. Merge Intervals
class Solution:
    def merge(self, nums: List[List[int]]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in nums:
            if len(ans)>0 and i[0]<=ans[-1][1]:
                ans[-1][1]=max(i[1], ans[-1][1])
            else:
                ans.append(i)
        return ans
