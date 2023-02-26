class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition_list(self, node, x):
        p=node
        head_st=ListNode(None)
        head_lt=ListNode(None)
        p1=head_st
        p2=head_lt
        while(p!=None):
            if p.val<x:
                p1.next=ListNode(p.val)
                p1=p1.next
            else:
                p2.next=ListNode(p.val)
                p2=p2.next
            p=p.next
        p1.next=head_lt.next
        return head_st.next

