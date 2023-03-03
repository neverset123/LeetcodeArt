# 判断两个字符串是否具有一样的形式
class Solution:
    def isIsomorphic_v1(self, s: str, t: str) -> bool:
        from collections import OrderedDict
        s_dict=OrderedDict()
        t_dict=OrderedDict()
        if len(s)!=len(t):
            return False
        for i, item in enumerate(s):
            s_dict[item]=s_dict.get(item, [])+[i]
        for i, item in enumerate(t):
            t_dict[item]=t_dict.get(item, [])+[i]
        if list(s_dict.values())==list(t_dict.values()):
            return True
        else:
            return False
    
    def isIsomorphic_v2(self, s: str, t: str) -> bool:
        return list(map(s.find, s))==list(map(t.find, t))
