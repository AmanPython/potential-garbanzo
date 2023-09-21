## ChatGPT Optimized Solution

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next or k == 0:
            return head

        # Step 1: Calculate the length of the linked list
        current = head
        length = 1
        while current.next:
            current = current.next
            length += 1

        # Step 2: Calculate the effective rotation value
        k = k % length
        if k == 0:
            return head

        # Step 3: Find the new tail and break the cycle
        current.next = head  # Make the list circular
        current = head
        for _ in range(length - k - 1):
            current = current.next

        # Step 4: Update the head and tail pointers
        new_head = current.next
        current.next = None

        return new_head
