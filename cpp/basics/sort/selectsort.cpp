#include <iostream>

class selectSort {
public:
    void sort(int arr[], int size) {
        for(int i=0; i<size; i++) {
            int min = i;
            for(int j=i+1; j<size; j++) {
                if(arr[j] < arr[min]) {
                    min = j;
                }
            }
            std::swap(arr[i], arr[min]);
        }
    }
};

int main() {
    int nums[] = {1, 3, 2, 5, 4};
    selectSort s;
    s.sort(nums, 5);
    for(int i=0; i<5; i++) {
        std::cout<<nums[i]<<" ";
    }
    std::cout<<std::endl;
    return 0;
}

