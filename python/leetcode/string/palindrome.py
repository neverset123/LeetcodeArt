class Solution:
    def isPalindrome_v1(self, s: str) -> bool:
        temp_list=[]
        for i in s.lower():
            if (i>="a" and i<="z") or (i>="0" and i<="9"):
                temp_list.append(i)
        j=0
        k=len(temp_list)-1
        while(j<=k):
            if(temp_list[j]!=temp_list[k]):
                return False
            j+=1
            k-=1
        return True
    
    def is_palindrome(self, s):
        s_alnum = filter(str.isalnum, s.lower())
        return s_alnum == s_alnum[::-1]
    
    def validPalindrome(self, s: str) -> bool:
        if s==s[::-1]:
            return True
        else:
            i=0
            j=len(s)-1
            while(i<=j):
                if s[i]!=s[j]:
                    substring1=s[i:j]
                    substring2=s[i+1:j+1]
                    return (substring1==substring1[::-1] 
                            or substring2==substring2[::-1] )
                i+=1
                j-=1
            return True

    # length of the longest palindrome that can be built with the characters in the string
    def longest_palindrome(self, s: str) -> int:
        from collections import Counter
        res=0
        sc=Counter(s)
        for value in sc.values():
            res+=value//2
        if res*2<len(s):
            return res*2+1
        else:
            return res*2
            
if __name__ == "__main__":
    test_string = "cbabadcbb"
    solution = Solution()
    print(solution.longest_palindrome(test_string))
