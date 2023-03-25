import sys

class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        memo=[[-1]*n for _ in range(k)]
        def dp(k_1,n_1):
            if k_1==1:
                return n_1
            if n_1==0:
                return 0
            if memo[k_1-1][n_1-1]!=-1:
                return memo[k_1-1][n_1-1]
            res=sys.maxsize
            for i in range(1,n_1+1):
                res=min(res, max(dp(k_1-1, i-1),
                                    dp(k_1, n_1-i))+1)
            memo[k_1-1][n_1-1]=res
            return memo[k_1-1][n_1-1]
        return dp(k, n)

    #二分搜索代替线性搜索
    def superEggDrop_v1(self, k: int, n: int) -> int:
        memo=[[-1]*n for _ in range(k)]
        def dp(k_1,n_1):
            if k_1==1:
                return n_1
            if n_1==0:
                return 0
            if memo[k_1-1][n_1-1]!=-1:
                return memo[k_1-1][n_1-1]
            res=sys.maxsize
            lo, hi= 1, n_1
            while(lo<=hi):
                mid=(lo+hi)//2
                broken=dp(k_1-1, mid-1)
                not_broken=dp(k_1, n_1-mid)
                if broken>not_broken:
                    hi=mid-1
                    res=min(res, broken+1)
                else:
                    lo=mid+1
                    res=min(res, not_broken+1)
            memo[k_1-1][n_1-1]=res
            return memo[k_1-1][n_1-1]
        return dp(k, n)

if __name__ == "__main__":
    solution=Solution()
    k = 4
    n = 200
    print(solution.superEggDrop(k,n))