## Initial White Paper Solution

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # Step1 : Find the lenght of the list
        node = head 
        n = 0
        while node:
            node = node.next 
            n+=1 
        # Step2 : Update the end point 
        k = k % n
        end = n - (k + 1)
        node = head 
        while end > 0 :
            end -= 1
            node = node.next 
        start = node.next
        nex = start
        node.next = None 
        # Step3 : Connect the start point 
        while k > 1:
            k-= 1
            nex = nex.next 
        nex.next = head 
        return start