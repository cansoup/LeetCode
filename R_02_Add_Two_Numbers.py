# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr_one, curr_two, prev = l1, l2, None
        num_one, num_two, i, j, k = 0, 0, 0, 0, 0
        head = None
        
        while curr_one:
            num_one += curr_one.val * (10**i)
            next, curr_one.next = curr_one.next, prev
            prev, curr_one = curr_one, next
            i += 1

        while curr_two:
            num_two += curr_two.val * (10**j)
            next, curr_two.next = curr_two.next, prev
            prev, curr_two = curr_two, next
            j += 1
            
        sum = num_one + num_two
        
        for digit in str(sum):
            head = ListNode(int(digit), head)
            
        return head

