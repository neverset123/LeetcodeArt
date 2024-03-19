#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class permutation {
public:
    vector<vector<int>> res;
    vector<vector<int>> permute(vector<int>& nums) {
        vector<int> track;
        backtrack(nums, track);
        return res;
    }
    void backtrack(vector<int>& nums, vector<int>& track) {
        if (nums.size() == track.size()) {
            res.push_back(track);
            return;
        }
        for (int i = 0; i < nums.size(); i++) {
            if (find(track.begin(), track.end(), nums[i]) != track.end()) {
                continue;
            }
            track.push_back(nums[i]);
            backtrack(nums, track);
            track.pop_back();
        }
    }
};

int main() {
    vector<int> nums = {1, 2, 3};
    permutation p;
    vector<vector<int>> res = p.permute(nums);
    for (auto& r : res) { // auto& is used to avoid copying
        for (auto i : r) {
            cout << i << " ";
        }
        cout << endl;
    }
    return 0;
}

