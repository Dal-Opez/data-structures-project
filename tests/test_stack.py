"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Stack


class TestStack(unittest.TestCase):
    def test_push(self):
        test_stack = Stack()
        test_stack.push("One")
        self.assertEqual(test_stack.stack_list, ["One"])
        test_stack.push("Two")
        self.assertEqual(test_stack.stack_list, ["Two", "One"])

if __name__ == '__main__':
    unittest.main()