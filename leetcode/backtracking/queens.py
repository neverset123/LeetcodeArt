import copy
from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        if n==1:
            return [["Q"]]
        track= [["."]*n for _ in range(n)]
        def isValid(track, row, col):
            for i in range(n):
                if track[i][col]=="Q":
                    return False
            for i in range(n):
                if row-i >=0 and col+i<n:
                    if track[row-i][col+i]=="Q":
                        return False
            for i in range(n):
                if row-i>=0 and col-i>=0:
                    if track[row-i][col-i]=="Q":
                        return False
            return True

        def backtrack(track, row):
            print(n, row)
            if row==n:
                track_str =  []
                for i in range(n):
                    track_str.append("".join(track[i]))
                res.append(track_str)
                return
            for col in range(n):
                if not isValid(track, row, col):
                    continue
                track[row][col]="Q"
                backtrack(track, row+1)
                track[row][col]="."
        backtrack(track, 0)
        return res

if __name__=="__main__":
    n=4
    solution = Solution()
    print(solution.solveNQueens(n))
    
