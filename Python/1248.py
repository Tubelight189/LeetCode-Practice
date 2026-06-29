class Solution(object):
    def numberOfSubarrays(self, nums, k):
        def atmost(nums,k):
            l,r,ans,cnt=0,0,0,0
            for r in range(len(nums)):
                cnt+=nums[r]%2
                while cnt>k:
                    cnt-=nums[l]%2
                    l+=1
                ans+=(r-l+1)
            return ans
        return atmost(nums,k)-atmost(nums,k-1)    
