#Leetcode 53 - Maximum Subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mse = 0
        msf = float('-inf')
        
        for i in range(len(nums)):
            
            mse += nums[i]
            
            if mse < nums[i]:
                mse = nums[i]
                
            if msf<mse:
                msf=mse
        return msf
