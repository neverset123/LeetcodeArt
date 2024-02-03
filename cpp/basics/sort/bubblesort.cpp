
#include <iostream>

class bubbleSort{
    public:
    static void sort(int nums[], int size)
    {
        for(int i=0; i<size; i++)
        {
            for(int j=0; j<size-i-1; j++)
            {
                if(nums[j]>nums[j+1])
                {
                    std::swap(nums[j], nums[j+1]);
                }
            }
        }
    }    
};

int main()
{
    int nums[] = {1, 3, 2, 5, 4};
    bubbleSort::sort(nums, 5);
    for(int i=0; i<5; i++)
    {
        std::cout<<nums[i]<<" ";
    }
    std::cout<<std::endl;
    return 0;
}