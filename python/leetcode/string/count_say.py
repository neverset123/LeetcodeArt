class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        string=self.countAndSay(n-1)
        temp_list=[]
        temp_list1=[string[0]]
        for i in range(1,len(string)):
            if string[i-1]==string[i]:
                temp_list1.append(string[i])
            else:
                temp_list.append(temp_list1)
                temp_list1=[string[i]]
        temp_list.append(temp_list1)
        return "".join([str(len(i))+str(i[0]) for i in temp_list])


            