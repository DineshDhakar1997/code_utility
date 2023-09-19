class ListNode:
    def __init__(self, value=0, next=None):
        self.val = value
        self.next = next


def cllc(arr, pos):
    if not arr:
        return None

    # Create the linked list without a cycle
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next

    # Find the node at the specified position
    cycle_node = head
    for i in range(position):
        cycle_node = cycle_node.next

    # Create the cycle by connecting the last node to the specified position
    current.next = cycle_node

    return head


def check_ll(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False

# Example usage:
arr = [1, 2, 3, 4, 5]
position = 2
linked_list_with_cycle = cllc(arr, position)

print(check_ll(linked_list_with_cycle))  
