#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class left_right_pointer {
public:
    // 167. 两数之和 II - 输入有序数组, 只有一个答案
    vector<int> two_sum(vector<int>& nums, int target) {
        int left = 0, right = nums.size() - 1;
        while(left < right){
            int sum = nums[left] + nums[right];
            if(sum == target)
            {
                return {left, right};
            }
            else if(sum < target)
            {
                left++;
            }
            else
            {
                right--;
            }
        }
        return {-1, -1};
    }

    // 两数之和, 可能有多个答案
    vector<vector<int>> two_sum_target(vector<int>& nums, int target) 
    {
        sort(nums.begin(), nums.end());
        int left = 0, right = nums.size() - 1;
        vector<vector<int>> result;
        while(left < right){
            int sum = nums[left] + nums[right];
            if(sum == target)
            {
                result.push_back({nums[left], nums[right]});
                while(left < right && nums[left] == nums[left + 1]) left++; // 去重
                while(left < right && nums[right] == nums[right - 1]) right--; // 去重
                left++;
                right--;
            }
            else if(sum < target)
            {
                while(left < right && nums[left] == nums[left + 1]) left++;
                left++;
            }
            else
            {
                while(left < right && nums[right] == nums[right - 1]) right--;
                right--;
            }   
        }
        return result;
    }

    // 15. 三数之和
    vector<vector<int>> three_sum_target(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> result;
        for(int i = 0; i < nums.size(); i++)
        {
            if(i > 0 && nums[i] == nums[i - 1]) continue; // 去重
            int target = -nums[i];
            int left = i + 1, right = nums.size() - 1;
            while(left < right)
            {
                if(nums[left] + nums[right] == target)
                {
                    result.push_back({nums[i], nums[left], nums[right]});
                    while(left < right && nums[left] == nums[left + 1]) left++; // 去重
                    while(left < right && nums[right] == nums[right - 1]) right--; // 去重
                    left++;
                    right--;
                }
                else if(nums[left] + nums[right] < target)
                {
                    while(left < right && nums[left] == nums[left + 1]) left++;
                    left++;
                }
                else
                {
                    while(left < right && nums[right] == nums[right - 1]) right--;
                    right--;
                }
            }
        }
        return result;
    }
};

int main() {
    // vector<int> nums = {2, 7, 11, 15};
    // int target = 9;
    // vector<int> nums = {1, 3, 1, 2, 2, 3};
    // int target = 4;
    vector<int> nums = {-1, 0, 1, 2, -1, -4};
    int target = 0;
    left_right_pointer lrp;
    // vector<int> result = lrp.two_sum(nums, target);
    // cout << result[0] << " " << result[1] << endl;
    // vector<vector<int>> result = lrp.two_sum_target(nums, target);
    // while(!result.empty())
    // {
    //     vector<int> temp = result.back();
    //     result.pop_back();
    //     cout << temp[0] << " " << temp[1] << endl;
    // }
    vector<vector<int>> result = lrp.three_sum_target(nums);
    while(!result.empty())
    {
        vector<int> temp = result.back();
        result.pop_back();
        cout << temp[0] << " " << temp[1] << " " << temp[2] << endl;
    }
    return 0;
}
