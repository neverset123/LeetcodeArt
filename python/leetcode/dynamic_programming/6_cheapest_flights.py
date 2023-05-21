# 找到从出发城市飞往终点城市的最少费用， 最多转机次数为k
# 加权有向图中求最短路径

from collections import defaultdict
import sys
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # 中转次数转化为边数
        steps=k+1
        # 建立哈希表， to -> [from, price]
        temp_dict=defaultdict(list)
        m=len(flights)
        for i in range(m):
            if flights[i][1] not in temp_dict:
                temp_dict[flights[i][1]]=[]
            temp_dict[flights[i][1]].append((flights[i][0], flights[i][2]))
        memo=[[sys.maxsize]*steps for _ in range(n)] # n代表城市个数
        #dp返回终点为s，剩余步数为step的最小花费
        def dp(s, step):
            if s==src:
                return 0
            if step<=0:
                return -1
            if memo[s][step-1]!=sys.maxsize: #step 以1开头，所以需要减1
                return memo[s][step-1]
            res=sys.maxsize
            if s in temp_dict:
                # 遍历选择
                for item in temp_dict[s]:
                    next=dp(item[0], step-1)
                    if next!=-1:
                        res=min(res, item[1]+next)
            memo[s][step-1]=-1 if res==sys.maxsize else res
            return memo[s][step-1] 
        res=dp(dst, steps)
        return res

if __name__ == "__main__":
    solution=Solution()
    flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
    n=4
    k=1
    print(solution.findCheapestPrice(n,flights,0,3,k))