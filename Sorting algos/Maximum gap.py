#Leetcode 164 -  Maximum Gap

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        l=sorted(nums)
        ans=0
        for i in range(1,len(nums)):
            ans = max(ans,l[i]-l[i-1])
            
        return ans
