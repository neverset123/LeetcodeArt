#龙盘游戏

from collections import defaultdict
import sys

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        m=len(ring)
        n=len(key)
        memo=[[0]*n for _ in range(m)]
        # 创建哈希表
        ring_dict=defaultdict(list)
        for index, item in enumerate(ring):
            if item not in ring_dict:
                ring_dict[item]=[]
            ring_dict[item].append(index)
        # 计算圆盘指针在 ring[i]，输入 key[j..] 的最少操作数
        def dp(ring, key,i,j):
            if j == n:
                return 0
            if memo[i][j]!=0:
                return memo[i][j]
            res=sys.maxsize
            for k in ring_dict[key[j]]:
                # 顺时针和逆时针转动的最小步数
                steps=min(abs(k-i), abs(m-abs(k-i)))
                # 转动steps次+一次确认
                res=min(res, 1+steps+dp(ring,key,k,j+1))
            memo[i][j]=res
            return memo[i][j]
        return dp(ring, key,0,0)


if __name__ == "__main__":
    solution=Solution()
    ring="pqwcx"
    key="cpqwx"
    print(solution.findRotateSteps(ring,key))