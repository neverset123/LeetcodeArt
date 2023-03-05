class Solution:
    def detectCapitalUse_v1(self, word: str) -> bool:
        if word[0]==word[0].upper():
            return all(letter==letter.upper() for letter in word[1:]) or all(letter==letter.lower() for letter in word[1:])
        else:
            return all(letter==letter.lower() for letter in word[1:])
    
    def detectCapitalUse(self, word):
        return word.islower() or word.isupper() or word.istitle()