#209. Minimum Size Subarray Sum
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        a=0
        b=0
        s=0
        ans = float('inf')

        while(b<len(nums)):
            s+=nums[b]
            if(s>=target):
                while(s>=target):
                    s-=nums[a]
                    a+=1
                ans = min(b-a+2,ans)
                
            b+=1

        if ans == float('inf'):
            return 0
        else:return ans


        













        
