# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        pre = None
        cur = slow
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        while pre.next:
            nxt = head.next
            head.next = pre
            head = nxt

            nxt2 = pre.next
            pre.next = head
            pre = nxt2
        