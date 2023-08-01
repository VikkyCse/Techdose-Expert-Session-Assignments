#Leetcode 75 - Sort Colors

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        def part(arr,l,h):
            pivot = arr[l]
            i=l+1
            j=h

            while(i<=j):

                while(i<=j and pivot>=arr[i]):
                    i+=1
                while(i<=j and pivot<arr[j]):
                    j-=1
                if i<=j:
                    arr[i],arr[j] = arr[j],arr[i]
            arr[l],arr[j]=arr[j],arr[l]
            return j
        def qs(nums,l,h):
            if l<h:
                pi = part(nums,l,h)
                qs(nums,l,pi-1)
                qs(nums,pi+1,h)
        qs(nums,0,len(nums)-1)
