import itertools
def letterCasePermutation(self, S: 'str'):
    L = ((s.lower(), s.upper()) if s.isalpha() else s for s in S)
    # [('a', 'A'), '1', ('b', 'B'), '2']
    return [''.join(c) for c in itertools.product(*L)]