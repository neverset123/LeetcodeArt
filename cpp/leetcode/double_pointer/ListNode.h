#include <iostream>
#include <vector>

struct ListNode{
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

ListNode* buildList(std::vector<int> arr, int n)
{
    if(n == 0)
        return NULL;
    ListNode *head = new ListNode(arr[0]);
    ListNode *cur = head;
    for(int i = 1; i < n; i++)
    {
        cur->next = new ListNode(arr[i]);
        cur = cur->next;
    }
    return head;
}