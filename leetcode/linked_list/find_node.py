class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def last_kth_node(self, node, k):
        p_fast=node
        p_slow=node
        for i in range(k):
            p_fast=p_fast.next
        while(p_fast!=None):
            p_fast=p_fast.next
            p_slow=p_slow.next
        return p_slow
    
    def del_last_kth_node(self, node, k):
        dummy_node=ListNode(None)
        dummy_node.next=node
        temp_node=self.last_kth_node(dummy_node, k+1)
        temp_node.next=temp_node.next.next
        return dummy_node.next

    def middel_node(self, node):
        p_fast=node
        p_slow=node
        while(p_fast!=None and p_fast.next!=None):
            p_fast=p_fast.next.next
            p_slow=p_slow.next
        return p_slow
    
    def has_cycle(self, node):
        p_fast=node
        p_slow=node
        while(p_fast!=None and p_fast.next!=None):
            p_fast=p_fast.next.next
            p_slow=p_slow.next
            if p_slow==p_fast:
                break
        if p_fast==None or p_fast.next==None:
            return 
        p_slow=node
        while(p_slow!=p_fast):
            p_fast=p_fast.next
            p_slow=p_slow.next
        return p_slow

    def find_intersection(self, node1, node2):
        p1=node1
        p2=node2
        while(p1!=p2):
            if p1==None:
                p1=node2
            else: p1=p1.next
            if p2==None:
                p2=node1
            else: p2=p2.next
            
        return p1

if __name__ == "__main__":
    pass