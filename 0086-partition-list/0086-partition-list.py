# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(0)
        curr=dummy
        if not head:
            return dummy.next
        first_val=head.val
        numbers=[]
        numbers.append(first_val)
        next_vals=head.next
        while next_vals:
            numbers.append(next_vals.val)
            next_vals=next_vals.next
        res=[]
        for i in range(len(numbers)):
            if numbers[i]<x:
                res.append(numbers[i])
        for i in range(len(numbers)):
            if numbers[i]>=x:
                res.append(numbers[i])
        for num in res:
            new=ListNode(num)
            curr.next=new
            curr=curr.next
        return dummy.next