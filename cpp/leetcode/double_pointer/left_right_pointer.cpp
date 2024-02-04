#include <iostream>
#include <vector>
using namespace std;

class left_right_pointer {
public:
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

    
};

int main() {
    vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    left_right_pointer lrp;
    vector<int> result = lrp.two_sum(nums, target);
    cout << result[0] << " " << result[1] << endl;
    return 0;
}
