class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        i=0
        j=len(s)-1
        s_list=list(s)
        while(i<j):
            if not s[i].isalpha():
                i+=1
                continue
            if not s[j].isalpha():
                j-=1
                continue
            if i<j:
                s_list[i], s_list[j]=s_list[j], s_list[i]
            i+=1
            j-=1
        return "".join(s_list)
            
            
