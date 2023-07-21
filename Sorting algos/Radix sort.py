#radix sort

nums = [ 170, 45, 75, 90, 802, 24, 2, 66]
def counting_sort(nums,ex):

    count = [0 for i in range(10)]
    output = [0]*len(nums)
    n=len(nums)
    for i in nums:
        count[int(i)%ex]+=1
    for i in range(1,10):
        count[i]+=count[i-1]


    for i in range(n-1,-1,-1):
        output[count[nums[i]%ex]-1]=nums[i]
        count[nums[i]%ex]-=1
    print(output)
    
def radix_sort(nums):

    ele = max(nums)

    ex = 1
    
    while ele//ex >0:
        counting_sort(nums,ex)
        ex*=10
radix_sort(nums)
