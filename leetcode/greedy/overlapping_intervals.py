import sys
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        end=-sys.maxsize-1
        res=0
        for item in intervals:
            if item[0]>=end:
                end=item[1]
            else:
                res+=1
        return res
    
    