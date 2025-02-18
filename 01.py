class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"{self.value} -> {self.next}"


def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


def merge_sorted_lists(l1, l2):
    dummy = ListNode()
    tail = dummy

    while l1 and l2:
        if l1.value < l2.value:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    tail.next = l1 or l2
    return dummy.next


def merge_sort(head):
    if not head or not head.next:
        return head

    # Розділення списку на дві частини
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    mid = slow.next
    slow.next = None

    # Рекурсивне сортування
    left = merge_sort(head)
    right = merge_sort(mid)

    return merge_sorted_lists(left, right)


# Тестування:
def print_list(head):
    while head:
        print(head.value, end=" -> ")
        head = head.next
    print("None")


# Створюємо список: 3 -> 1 -> 4 -> 2
head = ListNode(3, ListNode(1, ListNode(4, ListNode(2))))

print("Оригінальний список:")
print_list(head)

# Тест реверсування
reversed_head = reverse_list(head)
print("\nРеверсований список:")
print_list(reversed_head)

# Тест сортування
sorted_head = merge_sort(reversed_head)
print("\nВідсортований список:")
print_list(sorted_head)

# Тест об’єднання двох відсортованих списків
list1 = ListNode(1, ListNode(3, ListNode(5)))
list2 = ListNode(2, ListNode(4, ListNode(6)))
merged_head = merge_sorted_lists(list1, list2)
print("\nОб'єднаний список:")
print_list(merged_head)
