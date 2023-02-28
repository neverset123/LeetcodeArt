class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse(self, node):
        if node==None or node.next==None:
            return node
        last_node=self.reverse(node.next)
        node.next.next=node
        node.next=None
        return last_node

    def reverse_v1(self, node):
        pre=None
        curr=node
        next=node
        while(curr!=None):
            next=curr.next
            curr.next=pre
            pre=curr
            curr=next
        return pre

    def reverseN(self, node, n):
        if n==1:
            successor=node.next
            return node
        last_node=self.reverseN(node.next, n-1)
        node.next.next=node
        node.next=successor
        return last_node
    
    def reversetBetween(self, node, left, right):
        if left==1:
            return self.reversetN(node, right)
        node.next=self.reversetBetween(node.next, left-1, right-1)
        return node
    
    def reverseBetweenNode(self, node1, node2):
        pre=None
        curr=node1
        next=node1
        while(curr!=node2):
            next=curr.next
            curr.next=pre
            pre=curr
            curr=next
        return pre
    
    def reverseKGroup(self, node, k):
        if node==None:
            return
        node_left=node
        node_right=node
        for i in range(k):
            if node_right==None: 
                return node
            node_right=node_right.next
        head=self.reverseBetweenNode(node_left,node_right)
        node_left.next=self.reverseKGroup(node_right, k)
        return head



