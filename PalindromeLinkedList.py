# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = head
        fast = head
        stack = []
        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
            
        if fast:
            slow = slow.next
        
        while slow and stack:
            if slow.val != stack.pop():
                return False
            slow = slow.next
            
        return True