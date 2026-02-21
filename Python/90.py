def subsetsWithDup( nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums.sort()
    glist = [[]]
    llist = []
    start=0
    for i in range(0,len(nums)):
        if i>0 and nums[i]!=nums[i-1]:
           start=prevlength
        else: start=0
        prevlength=len(glist)

        for j in range(start,prevlength):
            glist.append(glist[j]+[nums[i]])
    return glist

nums = [1,2,2]#Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
print(subsetsWithDup(nums))