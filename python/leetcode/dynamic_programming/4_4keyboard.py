#通过4种按键的最多屏幕输出

class Solution:
    def maxA(self,m):
        dp=[0]*(m+1)
        #最后一次按键要么是A要么是C-V
        for i in range(1, m+1):
            #按A键
            dp[i]=dp[i-1]+1
            #全选+复制，连续粘贴i-j次
            for j in range(2, i):
                dp[i]=max(dp[i], dp[j-2]*(i-j+1))
        return dp[m]

if __name__ == "__main__":
    m=7
    solution=Solution()
    print(solution.maxA(m))