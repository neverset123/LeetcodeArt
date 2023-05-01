class Solution:
    def longestCommonPrefix(self, strs):
        pre=strs[0]
        k=1
        curr=""
        while(k<len(strs)):
            curr=strs[k]
            while(curr.find(pre)!=0):
                pre=pre[:len(pre)-1]
            if pre=="":
                return ""
            k+=1
        return pre  

if __name__ == "__main__":
    print("test".find("a"))
    print("E" in ["e"])