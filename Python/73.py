class Solution(object):
    def setZeroes(self, matrix):
        vflag,hflag=False,False
        for i in range(len(matrix)):
            if matrix[i][0]==0:
                vflag=True
        for i in range(len(matrix[0])):
            if matrix[0][i]==0:
                hflag=True
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
        if vflag:
            for i in range(len(matrix)):
                matrix[i][0]=0
        if hflag:
            for j in range(len(matrix[0])):
                matrix[0][j]=0
