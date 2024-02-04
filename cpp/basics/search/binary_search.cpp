#include <iostream>
#include <vector>

int binarySearch(std::vector<int>& nums, int target){
    int left=0;
    int right=nums.size()-1; // [0, nums.size()-1]闭区间搜索
    while(left<=right){ // <= [left, right]闭区间搜索
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

int left_boundary(std::vector<int>& nums, int target)
{
    int left=0;
    int right=nums.size()-1; // [0, nums.size()-1]闭区间搜索
    while(left<=right){ // <= [left, right]闭区间搜索
        int mid=left+(right-left)/2;
        if(target==nums[mid]){
            right=mid-1;
        }else if(target>nums[mid]){
            left=mid+1;
        }else if(target<nums[mid]){
            right=mid-1;    
        }
    }
    if(left>=nums.size() || nums[left]!=target){
        return -1;
    }
    return left;
}

int right_boundary(std::vector<int>& nums, int target)
{
    int left=0;
    int right=nums.size()-1; // [0, nums.size()-1]闭区间搜索
    while(left<=right){ // <= [left, right]闭区间搜索
        int mid=left+(right-left)/2;
        if(target==nums[mid]){
            left=mid+1;
        }else if(target>nums[mid]){
            left=mid+1;
        }else if(target<nums[mid]){
            right=mid-1;    
        }
    }
    if(right<0 || nums[right]!=target){
        return -1;
    }
    return right;
}

int main() {
  std::vector<int> test_data{1,3,3,3,5,9};
  std::cout<< right_boundary(test_data, 3)<<std::endl;
}