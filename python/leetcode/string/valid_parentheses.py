class Solution:
    def isValid(s):
        temp_dict={")":"(", "]":"[", "}":"{"}
        temp_list=[]
        for i in range(len(s)):
            if s[i] in temp_dict.values():
                temp_list.append(s[i])
            elif s[i] in temp_dict.keys():
                if len(temp_list)==0 or temp_list.pop()!=temp_dict[s[i]]:
                    return False
            else:
                return False
        return len(temp_list)==0

    def minAddToMakeValid(s):
        res=0
        temp_dict={")":"(", "]":"[", "}":"{"}
        temp_list=[]
        for i in range(len(s)):
            if s[i] in temp_dict.values():
                temp_list.append(s[i])
            elif s[i] in temp_dict.keys():
                if len(temp_list)==0 or temp_list.pop()!=temp_dict[s[i]]:
                    res+=1
        res+=len(temp_list)
        return res

if __name__ == "__main__":
    print([1,2,3].pop())