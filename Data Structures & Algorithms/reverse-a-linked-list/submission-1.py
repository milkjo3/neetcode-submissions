# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
            
        arr = []
        while head != None:
            arr.append(head.val)
            head = head.next

        r = len(arr) - 1
        for i in range(len(arr)//2):
            arr[i], arr[r] = arr[r], arr[i]
            r -= 1

        dummy = ListNode()
        current = dummy
        for i in range(0, len(arr)):
            current.next = ListNode(arr[i])
            current = current.next
        
        return dummy.next


