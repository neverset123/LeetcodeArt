//归并排序
#include <iostream>
#include <vector>

class mergeSort {
    public:
        static std::vector<int> temp;
        static void sort(int arr[], int left, int right) {
            if(left == right) return;
            int m = (right+left)/2;
            sort(arr, left, m);
            sort(arr, m+1, right);
            merge(arr, left, m, right); 
        }
        static void merge(int arr[], int left, int m, int right) {
            for(int i=left; i<=right; i++) temp[i] = arr[i];
            int i = left, j = m+1;
            for(int k=left; k<=right; k++)
            {
                if(i==m+1) arr[k] = temp[j++];
                else if(j==right+1) arr[k] = temp[i++];
                else if(temp[i] < temp[j]) arr[k] = temp[i++];
                else arr[k] = temp[j++];
            }
        }
};

std::vector<int> mergeSort::temp = std::vector<int>(10, 0);
int main(){
    int nums[] = {1, 3, 2, 5, 4};
    mergeSort::sort(nums, 0, 4);
    for(int i=0; i<5; i++){
        std::cout<<nums[i]<<" ";
    }
    std::cout<<std::endl;
    return 0;
}