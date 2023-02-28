class Solution:
    def strStr(str1, str2):
        for i in range(len(str1)-len(str2)+1):
            if str1[i:i+len(str2)]==str2:
                return i
        return -1