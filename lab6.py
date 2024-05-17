class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next

    def sort_list(self):
        if self.head is None:
            return

        new_head = None
        current = self.head

        while current:
            next_node = current.next
            if new_head is None or current.value <= new_head.value:
                current.next = new_head
                new_head = current
            else:
                search = new_head
                while search.next and search.next.value < current.value:
                    search = search.next
                current.next = search.next
                search.next = current
            current = next_node

        self.head = new_head

    def __str__(self):
        result = ""
        current_node = self.head
        while current_node:
            result += str(current_node.value) + " "
            current_node = current_node.next
        return result


if __name__ == '__main__':
    # Пример использования
    my_list = LinkedList()
    my_list.append(3)
    my_list.append(1)
    my_list.append(4)
    my_list.append(2)
    print(my_list)  # Output: 3 1 4 2
    my_list.sort_list()
    print(my_list)  # Output: 1 2 3 4
