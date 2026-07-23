def reverse_linkedList(head):
    previous = None
    current = head
    while current:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
    
    return previous


def middle_node(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def has_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            return True
        
    return False


def kth_from_end(head, k):
    slow = head
    fast = head

    # Create a gap of k nodes.
    for _ in range(k):
        if fast is None:
            return None  # k is larger than the list
        fast = fast.next

    # Preserve the gap.
    while fast:
        slow = slow.next
        fast = fast.next

    return slow


