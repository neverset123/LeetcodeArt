#include <iostream>
#include <vector>

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
            int pivot = nums[left];
            for(int i=left+1; i<=right; i++){
                if(nums[i]<pivot){
                    std::swap(nums[left], nums[i]);
                    left++;
                }
            }
            std::swap(nums[left], nums[right]);
            return left;
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