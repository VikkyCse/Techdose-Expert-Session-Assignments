#Counting Sort

nums = [5,2,7,1,4]

def counting_sort(nums):

    count = [0 for i in range(10)]
    output = [0]*len(nums)
    n=len(nums)
    for i in nums:
        count[i]+=1
    for i in range(1,10):
        count[i]+=count[i-1]


    for i in range(n-1,-1,-1):
        output[count[nums[i]]-1]=nums[i]
    print(output)
    
counting_sort(nums)
    
