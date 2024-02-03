#include <iostream>

class quickSort{
    public:
        static void sort(int nums[], int size){
            sort(nums, 0, size-1);
        }

    private:
        static void sort(int nums[], int left, int right){
            if(left>=right){
                return;
            }
            int pivot = partition(nums, left, right);
            sort(nums, left, pivot-1);
            sort(nums, pivot+1, right);
        }
        static int partition(int nums[], int left, int right){
            int pivot = left;
            while(left<right){
                while(left<right && nums[right]>nums[pivot]){
                    right--;
                }
                while(left<right && nums[left]<=nums[pivot]){
                    left++;
                }
                std::swap(nums[left], nums[right]);
            }
            std::swap(nums[pivot], nums[right]);
            return right;
        }
};

int main(){
    int nums[] = {1, 3, 2, 5, 4};
    quickSort::sort(nums, 5);
    for(int i=0; i<5; i++){
        std::cout<<nums[i]<<" ";
    }
    std::cout<<std::endl;
    return 0;
}