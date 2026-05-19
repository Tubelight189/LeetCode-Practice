class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left,right,ans=0,0,0
        map=dict()
        while right < len(s):
            if s[right] not in map:
                map[s[right]]=1
                right+=1
            else :
                del map[s[left]]
                left+=1
            ans=max(right-left,ans)            
        return ans