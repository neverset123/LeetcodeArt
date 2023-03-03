def canConstruct(self, ransomNote, magazine):
    for item in set(ransomNote):
        if magazine.count(item) < ransomNote.count(item):
            return False
    return True