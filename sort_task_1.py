class ListNode:
    def __init__(self, value=0, next_node=None):
        self.value = value
        self.next = next_node


def reverse_linked_list(head):
    prev_node = None
    current_node = head
    while current_node:
        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node
    return prev_node


def insertion_sort_linked_list(head):
    dummy = ListNode(float("-inf"))
    dummy.next = head
    last_sorted = head
    current = head.next
    while current:
        if last_sorted.value <= current.value:
            last_sorted = last_sorted.next
        else:
            prev = dummy
            while prev.next.value < current.value:
                prev = prev.next
            last_sorted.next = current.next
            current.next = prev.next
            prev.next = current
        current = last_sorted.next
    return dummy.next

def merge_sorted_linked_lists(l1, l2):
    dummy = ListNode()
    current = dummy
    while l1 and l2:
        if l1.value < l2.value:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    current.next = l1 if l1 else l2
    return dummy.next
def test_reverse_linked_list():
    # Створення тестового однозв'язного списку: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    # Реверсування списку
    reversed_head = reverse_linked_list(head)

    # Перевірка правильності реверсу
    assert reversed_head.value == 5
    assert reversed_head.next.value == 4
    assert reversed_head.next.next.value == 3
    assert reversed_head.next.next.next.value == 2
    assert reversed_head.next.next.next.next.value == 1
    assert reversed_head.next.next.next.next.next is None


def test_insertion_sort_linked_list():
    # Створення тестового однозв'язного списку: 3 -> 1 -> 4 -> 2 -> 5
    head = ListNode(3)
    head.next = ListNode(1)
    head.next.next = ListNode(4)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(5)

    # Сортування списку
    sorted_head = insertion_sort_linked_list(head)

    # Перевірка правильності сортування
    assert sorted_head.value == 1
    assert sorted_head.next.value == 2
    assert sorted_head.next.next.value == 3
    assert sorted_head.next.next.next.value == 4
    assert sorted_head.next.next.next.next.value == 5
    assert sorted_head.next.next.next.next.next is None


def test_merge_sorted_linked_lists():
    # Створення тестових однозв'язних списків: 1 -> 3 -> 5 та 2 -> 4 -> 6
    l1 = ListNode(1)
    l1.next = ListNode(3)
    l1.next.next = ListNode(5)

    l2 = ListNode(2)
    l2.next = ListNode(4)
    l2.next.next = ListNode(6)

    # Об'єднання списків
    merged_head = merge_sorted_linked_lists(l1, l2)

    # Перевірка правильності об'єднання
    assert merged_head.value == 1
    assert merged_head.next.value == 2
    assert merged_head.next.next.value == 3
    assert merged_head.next.next.next.value == 4
    assert merged_head.next.next.next.next.value == 5
    assert merged_head.next.next.next.next.next.value == 6
    assert merged_head.next.next.next.next.next.next is None


# Запуск тестів
test_reverse_linked_list()
test_insertion_sort_linked_list()
test_merge_sorted_linked_lists()
print("All tests passed successfully!")

