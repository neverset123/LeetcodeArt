class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m=len(s)
        n=len(p)
        memo=[[-1]*n for _ in range(m)]
        def dp(s, p, i, j):
            # base case
            if j==n:
                return i==m
            if i==m:
                if (n-j)%2==1:
                    return False
                for k in range(j, n, 2):
                    if p[k+1]!="*":
                        return False
                return True
            if memo[i][j]!=-1:
                return memo[i][j]
            res=False
            if s[i]==p[j] or p[j]==".":
                if j<n-1 and p[j+1]=="*":
                    res=(dp(s,p,i,j+2) or dp(s,p,i+1,j))
                else:
                    res=dp(s,p,i+1,j+1)
            else:
                if j<n-1 and p[j+1]=="*":
                    res=(dp(s,p,i,j+2))
                else:
                    res=False
            memo[i][j]=res
            return memo[i][j]
        return dp(s,p,0,0)
            
if __name__ == "__main__":
    solution=Solution()
    s = "aa"
    p = "a*"
    print(solution.isMatch(s,p))