class Solution:
    def minMeetingRooms(self, meetings):
        n=len(meetings)
        starts=[]
        ends=[]
        for meeting in meetings:
            starts.append(meeting[0])
            ends.append(meeting[1])
        starts.sort()
        ends.sort()
        i=0
        j=0
        count=0
        for _ in range(n*2):
            if starts[i]<ends[j] and i<n:
                count+=1
                i+=1
            else:
                count-=1
                j+=1
            res=max(res, count)
        return res