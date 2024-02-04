#include <iostream>
#include "leetcode/pointer/ListNode.h"

class fast_slow_pointer {
public:
    //  141. Linked List Cycle
    bool has_cycle(ListNode* head)
    {
        ListNode* fast, *slow;
        fast = slow = head;
        while(fast && fast->next)
        {
            fast = fast->next->next; // fast pointer moves 2 steps
            slow = slow->next;
            if(fast == slow)
                return true;
        }
        return false;
    }

    // 142. Linked List Cycle II
    // 当快慢指针相遇时，让其中任一个指针指向头节点，然后让它俩以相同速度前进，再次相遇时所在的节点位置就是环开始的位置
    ListNode* get_cycle_start(ListNode* head)
    {
        ListNode* fast, *slow;
        fast = slow = head;
        while(fast && fast->next)
        {
            fast = fast->next->next;
            slow = slow->next;
            if(fast == slow)
            {
                slow = head;
                while(fast!=slow)
                {
                    fast = fast->next;
                    slow = slow->next;
                }
            }
        return slow;
        }
    }

};

int main()
{
    std::vector<int> arr = {3, 2, 0, -4};
    ListNode* head = buildList(arr, arr.size());
    fast_slow_pointer fsp;
    std::cout << fsp.has_cycle(head) << std::endl;
    return 0;
}