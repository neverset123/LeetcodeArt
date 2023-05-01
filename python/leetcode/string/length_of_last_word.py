class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        temp_list=s.split(" ")
        for i in temp_list[::-1]:
            if i!="":
                return len(i)
        return 0