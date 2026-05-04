import unittest
import json
import os
from task_management import TaskManager, Task, User

class BaseTests(unittest.TestCase):

    def setUp(self):
        current_dir = os.path.dirname(__file__)
        task_manager.tasks = {}
        task_manager.users = {}

        # Load tasks
        with open(current_dir + "/data/tasks.json") as f:
            task_data = json.load(f)
            for k, v in task_data.items():
                task = Task(
                    v['id'],
                    v['title'],
                    v['description'],
                    v['status'],
                    v['assigned_user_ids']
                )
                task_manager.tasks[k] = task

        # Load users
        with open(current_dir + "/data/users.json") as f:
            user_data = json.load(f)
            for k, v in user_data.items():
                user = User(v['user_id'], v['first_name'], v['last_name'])
                task_manager.users[k] = user

    def test_count_tasks(self):
        self.assertEqual(1, len(task_manager.get_all_tasks()))

    def test_assign_user(self):
        task_id = list(task_manager.tasks.keys())[0]

        assigned_users = task_manager.tasks[task_id].assigned_user_ids
        user_ids = list(task_manager.users.keys())

        user_id = None
        for u in user_ids:
            if u not in assigned_users:
                user_id = u
                break

        result = task_manager.assign_user(task_id, user_id)
        self.assertIn(user_id, result)

    def test_assign_existing_user(self):
        task_id = list(task_manager.tasks.keys())[0]
        user_id = task_manager.tasks[task_id].assigned_user_ids[0]

        result = task_manager.assign_user(task_id, user_id)
        self.assertIn("already assigned", result)

    def test_remove_user(self):
        task_id = list(task_manager.tasks.keys())[0]
        user_id = task_manager.tasks[task_id].assigned_user_ids[0]

        result = task_manager.remove_user(task_id, user_id)
        self.assertNotIn(user_id, result)

    def test_remove_user_nonexisting(self):
        result = task_manager.remove_user("1", "1")
        self.assertEqual("Task does not exist.", result)

    def test_nonexistent_user(self):
        task_id = list(task_manager.tasks.keys())[0]
        result = task_manager.assign_user(task_id, "invalid_user")
        self.assertIn("does not exist", result)


if __name__ == "__main__":
    task_manager = TaskManager()
    unittest.main()