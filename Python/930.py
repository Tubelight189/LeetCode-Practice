class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        def atMost(nums,goal):
            if goal<0:return 0
            left,right,ans=0,0,0
            csum=0
            while right<(len(nums)):
                csum+=nums[right]
                while csum>goal:
                    csum-=nums[left]
                    left+=1
                ans+=(right-left+1)
                right+=1
            return ans
        return atMost(nums, goal) - atMost(nums, goal - 1)
