def loop_size(head):
    # Check for edge cases (empty list or only one node)
    if not head or not head.next:
        return 0  # No loop possible
    
    # Step 1: Detect the loop using slow and fast pointers
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next  # Move slow pointer by one
        fast = fast.next.next  # Move fast pointer by two

        # If slow and fast meet, we found a loop
        if slow == fast:
            # Step 2: Calculate loop size
            size = 1
            current = slow.next  # Move to the next node to start counting
            while current != slow:
                size += 1
                current = current.next
            return size

    # If no loop is found, return 0
    return 0