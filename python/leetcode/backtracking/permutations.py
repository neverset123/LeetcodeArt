# 生成全排列
from typing import List
import copy

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        track=[]
        def backtrack(nums, track):
            if len(track)==len(nums):
                res.append(copy.deepcopy(track))
                return
            for item in nums:
                if item in track:
                    continue
                track.append(item)
                backtrack(nums, track)
                track.pop(-1)
        backtrack(nums, track)
        return res