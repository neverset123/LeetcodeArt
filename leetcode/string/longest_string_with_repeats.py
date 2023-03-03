class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        temp_list=[]
        len_max=0
        for i in range(len(s)):
            if s[i] in temp_list:
                len_max=max(len_max, len(temp_list))
                for j in range(len(temp_list)):
                    if temp_list[j]==s[i]:
                        break
                temp_list=temp_list[j+1:]
                temp_list.append(s[i])
            else:
                temp_list.append(s[i])
        len_max=max(len_max, len(temp_list))
        return len_max
