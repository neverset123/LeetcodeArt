#include <iostream>
#include <vector>
using namespace std;

int binarySearch(vector<int>& nums, int target){
    int left=0;
    int right=nums.size()-1;
    while(left<=right){
        int mid=left+(right-left)/2;
        if(target==nums[mid]){
            return mid;
        }else if(target>nums[mid]){
            left=mid+1;
        }else if(target<nums[mid]){
            right=mid-1;
        }
    }
    return -1;
}



int main() {
  vector<int> test_data{1,3,5,9};
  cout<< binarySearch(test_data, 5)<<endl;
}