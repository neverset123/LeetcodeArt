#include <iostream>
#include <unordered_map>
#include <string>

class left_right_pointers {
public:
    // 76. 最小覆盖子串
    std::string minWindow(std::string s, std::string t)
    {
        std::unordered_map<char, int> need, window;
        for (char c : t) need[c]++;    // 统计t中字符出现的次数
        int left = 0, right = 0;
        int valid = 0; // 记录窗口中满足need条件的字符个数
        int start = 0, len = INT_MAX; // 记录最小覆盖子串的起始索引及长度
        while(right < s.size()) //[left, right)
        {
            char c = s[right];
            right++;
            if(need.count(c)) // 判断右侧窗口是否要扩张
            {
                window[c]++;
                if(window[c] == need[c])
                {
                    valid++;
                }
            }
            while(valid == need.size()) // 判断左侧窗口是否要收缩
            {
                if(right - left < len)  // 更新最小覆盖子串
                {
                    start = left;
                    len = right - left;
                }
                char d = s[left];
                left++;
                if(need.count(d)) 
                {
                    if(window[d] == need[d])
                    {
                        valid--;
                    }
                    window[d]--;
                }
            }
        }
        return len == INT_MAX ? "" : s.substr(start, len);
    }

    // 567. 字符串的排列
    bool check_permutation(std::string s1, std::string s2)
    {
        std::string sub_str = minWindow(s1, s2);
        if( sub_str != "" && sub_str.size() == s2.size())
        {
            return true;
        }
        
        return false;
    }
};


int main()
{
    left_right_pointers lrp;
    // std::string s = "ADOBECODEBANC";
    // std::string t = "ABC";
    // std::string res = lrp.minWindow(s, t);
    std::string s1 = "ab";
    std::string s2 = "eidboaooo";
    bool res = lrp.check_permutation(s1, s2);
    std::cout << res << std::endl;
    return 0;
}
