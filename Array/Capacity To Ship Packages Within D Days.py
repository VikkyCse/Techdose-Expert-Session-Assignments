#1011. Capacity To Ship Packages Within D Days
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        l=max(weights)
        h=sum(weights)

        while(l<h):

            mid = (l+h)//2

            td = 1
            c = 0

            for i in weights:
                c+=i
                if c>mid:
                    td+=1
                    c=i
            if td<=days :
                h=mid
            else:
                l=mid+1
        return l
