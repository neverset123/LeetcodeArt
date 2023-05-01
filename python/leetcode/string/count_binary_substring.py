def countBinarySubstrings(self, s):
    res, prev, cur = 0, 0, 1
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            res += min(prev, cur)
            prev, cur = cur, 1
        else:
            cur += 1
    return res + min(prev, cur)