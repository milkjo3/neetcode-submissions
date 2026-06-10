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
        while head.next != None:
            arr.append(head.val)
            head = head.next
        arr.append(head.val)
        r = len(arr) - 1
        for i in range(len(arr)//2):
            arr[i], arr[r] = arr[r], arr[i]
            r -= 1
            
        dummy = ListNode()
        new = ListNode(arr[0])
        dummy.next = new
        for i in range(1, len(arr)):
            new.next = ListNode(arr[i])
            new = new.next
        
        return dummy.next


