"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Stack


class TestStack(unittest.TestCase):
    def test_push(self):
        test_stack_push = Stack()
        test_stack_push.push("One")
        self.assertEqual(test_stack_push.top.data, "One")
        test_stack_push.push("Two")
        self.assertEqual(test_stack_push.top.data, "Two")
        self.assertEqual(test_stack_push.top.next_node.data, "One")

    def test_pop(self):
        test_stack_pop = Stack()
        test_stack_pop.push("One")
        test_stack_pop.push("Two")
        self.assertEqual(test_stack_pop.pop(), "Two")
        self.assertEqual(test_stack_pop.pop(), "One")


if __name__ == '__main__':
    unittest.main()