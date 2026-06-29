class Solution(object):
    def numberOfSubstrings(self, s):
        left,right,ans=0,0,0
        map=defaultdict(int)
        for right in range(len(s)):
            map[s[right]]=right
            if len(map)==3:
                left=min(map.values())
                ans+=left+1
        return ans
