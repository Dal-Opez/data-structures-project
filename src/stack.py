
class Node:
    """Класс для узла стека"""
    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        return f"{self.next_node}"

class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.top = None

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        next_node = self.top
        new_top = Node(data, next_node)
        self.top = new_top

    def __str__(self):
        current = self.top
        items = []
        while current:
            items.append(current.data)
            current = current.next_node
        return f'Stack({", ".join(items)})'

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        data = self.top.data
        self.top = self.top.next_node
        return data

