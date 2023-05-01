class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        res=[]
        list1=list("qwertyuiop")
        list2=list("asdfghjkl")
        list3=list("zxcvbnm")
        for word in words:
            if all(letter.lower() in list1 for letter in word) or all(letter.lower() in list2 for letter in word) or all(letter.lower() in list3 for letter in word):
                res.append(word)
        return res