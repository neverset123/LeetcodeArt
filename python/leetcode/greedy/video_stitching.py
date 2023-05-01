class Solution:
    def videoStitching(self, clips, T):
        if T==0:
            return 0
        n=len(clips)
        clips.sort(key=lambda x: (x[0], -x[1]))
        curEnd=clips[0][1]
        nextEnd=0
        i=0
        res=1
        while(i<n):
            while(i<n):
                if clips[i][0]<curEnd:
                    nextEnd=max(nextEnd, clips[i][1])
                    i+=1
                else:
                    break
            res+=1
            curEnd=nextEnd
            if curEnd>=T:
                return res
        return -1
    
if __name__ == "__main__":
    clips=[[0,2], [4,6], [8,10], [1,9],[1,5],[5,9]]
    T=10
    solution=Solution()
    print(solution.videoStitching(clips, T))