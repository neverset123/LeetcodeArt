class Solution:
    def rotatedDigits(self, n: int) -> int:
        if n==0:
            return 0
        valid_digitals=["2", "5", "6", "9"]
        invalid_digitals=["3","4","7"]
        n_list=list(str(n))
        num=self.rotatedDigits(n-1)
        if any(item in invalid_digitals for item in n_list) or not any(item in valid_digitals for item in n_list):
            return num
        else:
            return num+1

