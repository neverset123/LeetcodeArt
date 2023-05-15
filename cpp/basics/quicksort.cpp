#include <iostream>
#include <vector>

class quickSort{
    public:
        static void sort(int nums[]){
            int size = sizeof(nums)/sizeof(nums[0]);
            sort(nums, 0, size-1);
        }

    private:
        static void sort(int nums[], int left, int right){
            if(left<right){
                return;
            }
            int pivot = partition()
        }
        static int partition(int nums[], int left, int right){
            
        }
}