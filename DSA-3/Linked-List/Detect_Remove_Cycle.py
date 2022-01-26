from Check_cycle_LL import linkedListCycle

def detectAndRemoveCycle(head):
    # This function returns slow pointer in cycle, if present
    slow = linkedListCycle(head)
    
    if slow:
        temp = slow
        # Counts number of nodes in the loop
        k = 1
        while temp.next != slow:
            temp = temp.next
            k += 1

        # set temp to head and move both pointers at same speed
        temp = head
        while temp != slow:
            slow = slow.next
            temp = temp.next
        
        # move one pointer to find the last node in cycle
        while temp.next != slow:
            temp = temp.next
        
        temp.next = None
        return "true"