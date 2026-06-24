class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def sol(a,b,index):
            if index==len(word):
                return True
            if a<0 or b<0 or a>=len(board) or b>=len(board[0]) or board[a][b]!=word[index]:return False
            ch=board[a][b]
            board[a][b]='#'
            found=(
            sol(a+1,b,index+1)or
            sol(a,b+1,index+1)or
            sol(a-1,b,index+1)or
            sol(a,b-1,index+1)
            )
            board[a][b]=ch
            return found
        for a in range(len(board)):
            for b in range(len(board[0])):
                if sol(a,b,0):return True
        return False
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(Solution().exist(board,word))