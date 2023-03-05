class Solution:
    def uniqueMorseRepresentations(self, words) -> int:
        transform_list=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        temp_set=set()
        for word in words:
            temp_set.add("".join([transform_list[ord(letter)-ord("a")] for letter in word]))
        return len(temp_set)

