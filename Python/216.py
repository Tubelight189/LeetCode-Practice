

def combinationSum3(k, n):
    result=[]
    def backtrack(k,n,path,start):
        if k==0 and n==0:
            result.append(path[:])
            return
        for i in range(start,10):
            if i>n or k<=0:break
            path.append(i)
            backtrack(k-1,n-i,path,i+1)
            path.pop()
        return result
    backtrack(k,n,[],1)
    return result
print(combinationSum3(3,7))