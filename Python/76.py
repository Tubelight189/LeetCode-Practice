
def minWindow(s, t):
    # if t not in s:return ""
    right, left, have, ans, maps, window, res = 0, 0, 0, float("inf"), {}, {}, ""
    # maps=dict()
    # res=""
    for right in t:maps[right]=maps.get(right,0)+1
    need=len(maps)
    # window = {}

    right,left,have,need,ans=0,0,0,len(maps),float("inf")

    for right in range(len(s)):
        c=s[right]
        window[c]=window.get(c,0)+1

        if c in maps and maps[c]==window[c]:have+=1

        while have==need:
            if right-left+1<ans:
                ans=right-left+1
                res=s[left:right+1]

            window[s[left]]-=1

            if s[left] in maps and window[s[left]]<maps[s[left]]:have-=1
            left+=1
    return res

s = "ADOBECODEBANC"
t = "ABC"
print(len(s))
print(minWindow(s,t))