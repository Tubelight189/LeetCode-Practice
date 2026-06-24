class Solution(object):
    def longestOnes(self, nums, k):
        zeros,left,right,ans=k,0,0,0
        for right in range(len(nums)):
            if nums[right]==0:
                if zeros==0:
                    while nums[left]==1:left+=1
                    if nums[left]==0:zeros+=1
                    left+=1
                zeros-=1
            ans=max(ans,right-left+1)
        return ans

