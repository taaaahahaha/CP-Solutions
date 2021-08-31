# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        t1,t2 = l1,l2
        n1 = ""
        while l1 != None:
            n1 += str(l1.val)
            l1 = l1.next
        n2 = ""
        while l2 != None:
            n2 += str(l2.val)
            l2 = l2.next
        sum = int(n1[::-1]) + int(n2[::-1])
        
        newnode = ListNode()
        temp = newnode
        while sum>0:
            temp.val = sum%10
            sum = sum//10
            if sum!=0:
                t1 = ListNode()
                temp.next = t1
                temp = temp.next
        
        
        
        return newnode
            
            