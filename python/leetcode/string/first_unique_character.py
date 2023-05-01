class Solution:
    def firstUniqChar_v1(self, s: str) -> int:
        index_dict={}
        times_dict={}
        for i in range(len(s)):
            if s[i] in index_dict:
                times_dict[s[i]]+=1
            else:
                times_dict[s[i]]=1
                index_dict[s[i]]=i
        min_index=-1
        for j in times_dict:
            if times_dict[j]==1 and min_index==-1:
                min_index=index_dict[j]
            elif times_dict[j]==1 and min_index!=-1:
                min_index=min(min_index, index_dict[j])
        return min_index
    
    def firstUniqChar(self, s):
        from collections import Counter
        c = Counter(s)
        for i, ch in enumerate(s):
            if c[ch] == 1:
                return i
        return -1
