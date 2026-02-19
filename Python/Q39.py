class Solution(object):
    def combinationSum(self, candidates, target):
        result=[]
        def sol(start, target,path):
            if target==0:
                result.append(path[:])
                return
            if target<0: return
            for i in range(start,len(candidates)):
                path.append(candidates[i])
                sol(i,target-candidates[i],path)
                path.pop()
        sol(0,target,[])
        return result



candidates = [2, 3, 6, 7]
target = 7
print(Solution().combinationSum(candidates, target))