"""
We use extra pointers so that we don't lose the head pointer
"""
def linkedListCycle(head):
    slow, fast = head, head

    while slow or fast:
        try:
            if fast.next.next:
                fast = fast.next.next
            if slow.next:
                slow = slow.next
        except:
            return False

        if slow == fast:
            return True