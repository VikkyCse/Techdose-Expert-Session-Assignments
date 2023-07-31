#radix sort

nums = [ 170, 45, 75, 90, 802, 24, 2, 66]
def counting_sort(nums,ex):

    count = [0 for i in range(10)]
    output = [0]*len(nums)
    n=len(nums)
    for i in nums:
        index = (i//ex)
        count[int(index%10)] += 1
    for i in range(1,10):
        count[i]+=count[i-1]

    i=n-1
    while i>=0:
        index = (nums[i]/ex)
        output[count[int(index%10)]-1]=nums[i]
        count[int((index)%10)] -= 1
        i-=1
    print(output)

    for i in range(0,len(nums)):
        nums[i] = output[i]
    
def radix_sort(nums):

    ele = max(nums)

    ex = 1
    
    while ele//ex >0:
        counting_sort(nums,ex)
        ex*=10
radix_sort(nums)
