def mostCommonWord(self, paragraph: 'str', banned: 'List[str]') -> 'str':
    import re
    import collections
    words = re.findall(r'\w+', paragraph.lower())
    c = collections.Counter(words)
    banned = set(banned)
    for word, count in c.most_common():
        if word and word not in banned:
            return word
    return ''