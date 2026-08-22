# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ans = ListNode(0)
        temp = ans
        carry = 0
        while l1 or l2 or carry:
            if l1:
                a = l1.val
            else:
                a = 0
            if l2:
                b = l2.val
            else:
                b = 0
            total = a + b + carry
            carry = total // 10
            digit = total % 10
            temp.next = ListNode(digit)
            temp = temp.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return ans.next