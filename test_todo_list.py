import unittest
from todo_list import TodoList

class TestTodoList(unittest.TestCase):
    def test_add_task(self):
        todo_list = TodoList()
        todo_list.add_task("Task 1")
        self.assertEqual(todo_list.tasks, ["Task 1"])

    def test_mark_task_as_completed(self):
        todo_list = TodoList()
        todo_list.add_task("Task 1")
        todo_list.mark_task_as_completed("Task 1")
        self.assertTrue(todo_list.is_task_completed("Task 1"))

    def test_delete_task(self):
        todo_list = TodoList()
        todo_list.add_task("Task 1")
        todo_list.delete_task("Task 1")
        self.assertEqual(todo_list.tasks, [])

if __name__ == "__main__":
    unittest.main()
