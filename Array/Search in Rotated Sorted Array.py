#33. Search in Rotated Sorted Array
class Solution:
    def search(self, nums: List[int], key: int) -> int:


        
        l=0
        h=len(nums)-1
        while l<=h:   
            mid = (l+h)//2
            if nums[mid]==key:
                return mid
            if nums[l] <= nums[mid]:
                if nums[l] <= key <nums[mid]:
                    h=mid-1
                else:
                   l=mid+1
            else:
                if nums[mid]<key<=nums[h]:
                    l=mid+1
                   
                else:
                    h=mid-1
        
        return -1
