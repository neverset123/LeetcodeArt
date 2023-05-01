from typing import List

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res=0
        temp_list=[]
        for i in range(len(colors)-1):
            if colors[i]==colors[i+1]:
                temp_list.append(neededTime[i])
            else:
                if len(temp_list)>=1:
                    temp_list.append(neededTime[i])
                    res+=(sum(temp_list)-max(temp_list))
                    temp_list=[]
            #print(temp_list)
        if colors[-1]==colors[-2]:
            temp_list.append(neededTime[-1])
            res+=(sum(temp_list)-max(temp_list))

        return res
