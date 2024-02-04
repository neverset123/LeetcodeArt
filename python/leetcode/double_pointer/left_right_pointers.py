# 时间复杂度：O(n)

class Solution:
    def two_sum(self, numbers, target):
        left = 0
        right = len(numbers)-1
        while(left<right):
            current = numbers[left]+numbers[right]
            if current==target:
                return [left+1, right+1]
            elif current<target:
                left+=1
            elif current>target:
                right-=1
        return [-1,-1]

    # longest palindrome substring
    def longest_palindrome(self, string):
        max_pali=""
        for i in range(len(string)):
            pali=self.palindrome(string, i, i)
            if len(pali)>len(max_pali):
                max_pali=pali
            pali=self.palindrome(string, i, i+1)
            if len(pali)>len(max_pali):
                max_pali=pali
        return max_pali

    def palindrome(self, string, left, right):
        while(left>=0 and right<len(string) and string[left]==string[right]):
            left-=1
            right+=1
        return string[left+1:right]

if __name__ == "__main__":
    test_data = [2,7,11,15]
    test_string = "babad"
    target=18
    solution = Solution()
    print(solution.two_sum(test_data, target))
    print(solution.longest_palindrome(test_string))
