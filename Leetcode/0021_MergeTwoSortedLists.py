class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        li = ListNode()
        head = li
        while l1 and l2:
            a = l1.val
            b = l2.val
            if a<b:
                li.next = ListNode(a)
                l1 = l1.next
            else:
                li.next = ListNode(b)
                l2 = l2.next
            li = li.next
        
        if not l1 and l2:
            while l2:
                li.next = ListNode(l2.val)
                l2 = l2.next
                li = li.next
        else:
            while l1:
                li.next = ListNode(l1.val)
                l1 = l1.next
                li = li.next
        return head.next
                