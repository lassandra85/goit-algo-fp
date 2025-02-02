class Node:
    """Вузол однозв'язного списку"""
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    """Однозв'язний список"""
    def __init__(self):
        self.head = None

    def append(self, value):
        """Додає елемент у кінець списку"""
        if not self.head:
            self.head = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)

    def print_list(self):
        """Виводить список"""
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        """Реверсує список (зміна посилань між вузлами)"""
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def merge_sort(self):
        """Сортування списку злиттям"""
        if not self.head or not self.head.next:
            return self.head

        def split(head):
            """Розділення списку на дві частини"""
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            middle = slow.next
            slow.next = None
            return head, middle

        def merge(left, right):
            """Злиття двох відсортованих списків"""
            dummy = Node(0)
            tail = dummy
            while left and right:
                if left.value < right.value:
                    tail.next, left = left, left.next
                else:
                    tail.next, right = right, right.next
                tail = tail.next
            tail.next = left or right
            return dummy.next

        def merge_sort_recursive(node):
            """Рекурсивний алгоритм сортування злиттям"""
            if not node or not node.next:
                return node
            left, right = split(node)
            left = merge_sort_recursive(left)
            right = merge_sort_recursive(right)
            return merge(left, right)

        self.head = merge_sort_recursive(self.head)

    @staticmethod
    def merge_sorted_lists(list1, list2):
        """Об'єднання двох відсортованих списків у один відсортований"""
        dummy = Node(0)
        tail = dummy
        while list1 and list2:
            if list1.value < list2.value:
                tail.next, list1 = list1, list1.next
            else:
                tail.next, list2 = list2, list2.next
            tail = tail.next
        tail.next = list1 or list2
        return dummy.next

# Тестування
list1 = LinkedList()
list1.append(3)
list1.append(1)
list1.append(4)
list1.append(2)
print("Початковий список:")
list1.print_list()

print("\nРеверсований список:")
list1.reverse()
list1.print_list()

print("\nСортування списку злиттям:")
list1.merge_sort()
list1.print_list()

# Створення двох відсортованих списків і їх об'єднання
list2 = LinkedList()
list2.append(1)
list2.append(3)
list2.append(5)

list3 = LinkedList()
list3.append(2)
list3.append(4)
list3.append(6)

merged_head = LinkedList.merge_sorted_lists(list2.head, list3.head)
merged_list = LinkedList()
merged_list.head = merged_head
print("\nОб'єднаний відсортований список:")
merged_list.print_list()