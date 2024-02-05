class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def merge_two_list(self, node1, node2):
        head=ListNode(None)
        temp_node=head
        p1=node1
        p2=node2
        while(p1!=None and p2!=None):
            if(p1.val<p2.val):
                temp_node.next=p1
                p1=p1.next
            else:
                temp_node.next=p2
                p2=p2.next
            temp_node=temp_node.next
        if p2!=None:
            temp_node.next=p2
        elif p1!=None:
            temp_node.next=p1
        return head.next
        
    def merge_multi_list_v1(self, list):
        if len(list)==0:
            return None
        head=None
        for i in range(len(list)):
            head=self.merge_two_list(head, list[i])
        return head

    def merge_multi_list(self, list):
        if len(list)==0:
            return None
        if len(list)==1:
            return list[0]
        mid=len(list)//2
        left=self.merge_multi_list(list[:mid])
        right=self.merge_multi_list(list[mid:])
        return self.merge_two_list(left, right)