#回文构词
def is_anagram(s, t):
    return sorted(s) == sorted(t)

def is_anagram_v1(s, t):
    from collections import Counter
    c1 = Counter(s)
    c2 = Counter(t)
    return c1 == c2

def find_all_anagram(s, p):
    from collections import Counter
    if len(s)<len(p):
        return []
    n=len(p)
    res=[]
    cp=Counter(p)
    cs=Counter(s[:n-1])
    for i in range(len(s)-n+1):
        if s[n-1+i] in cs:
            cs[s[n-1+i]]+=1
        else:
            cs[s[n-1+i]]=1
        if cp==cs:
            res.append(i)
        cs[s[i]]-=1
        if cs[s[i]]==0:
            del cs[s[i]]
    return res