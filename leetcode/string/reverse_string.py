class Solution:
    def reverseStr(self, s, k):
        letters = list(s)
        n = len(letters)
        # for i in range(n//(2*k)+1):
            # letters[2*k*i:k+2*k*i] = reversed(letters[2*k*i:k+2*k*i])
        for i in range(0, n, 2*k):
            letters[i:k+i] = reversed(letters[i:k+i])
        return ''.join(letters)