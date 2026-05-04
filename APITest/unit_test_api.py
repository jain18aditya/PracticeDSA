import unittest
import requests

BASE_URL = "http://localhost:8080/qa-task-management"

class BaseAPITests(unittest.TestCase):

    API_KEY = "codeSignal-api-key"

    @classmethod
    def send_get(cls, endpoint):
        return requests.get(
            BASE_URL + endpoint,
            headers={
                "Content-Type": "application/json",
                "API-Key": cls.API_KEY
            }
        )

    @classmethod
    def send_post(cls, endpoint, data):
        return requests.post(
            BASE_URL + endpoint,
            json=data,
            headers={
                "Content-Type": "application/json",
                "API-Key": cls.API_KEY
            }
        )

    @classmethod
    def send_patch(cls, endpoint, data):
        return requests.patch(
            BASE_URL + endpoint,
            json=data,
            headers={
                "Content-Type": "application/json",
                "API-Key": cls.API_KEY
            }
        )

    # ---------------- BASIC TESTS ---------------- #

    def test_get_all_tasks(self):
        res = self.send_get("/tasks")
        data = res.json()

        self.assertEqual(200, res.status_code)
        self.assertIn("tasks", data)

    def test_get_single_task(self):
        res = self.send_get("/tasks")
        task_id = res.json()["tasks"][0]["task_id"]

        res = self.send_get(f"/tasks/{task_id}")
        data = res.json()

        self.assertEqual(200, res.status_code)
        self.assertIn("task", data)
        self.assertEqual(task_id, data["task"]["task_id"])

    def test_get_invalid_task(self):
        res = self.send_get("/tasks/invalid")
        self.assertNotEqual(200, res.status_code)

    # ---------------- PATCH TESTS ---------------- #

    def test_patch_updates_task(self):
        res = self.send_get("/tasks")
        task_id = res.json()["tasks"][0]["task_id"]

        payload = {"status": "completed"}
        res = self.send_patch(f"/tasks/{task_id}", payload)

        self.assertEqual(200, res.status_code)

        # VERIFY update actually happened
        res = self.send_get(f"/tasks/{task_id}")
        self.assertEqual("completed", res.json()["task"]["status"])

    def test_patch_invalid_task(self):
        payload = {"status": "completed"}
        res = self.send_patch("/tasks/invalid", payload)

        self.assertNotEqual(200, res.status_code)

    # ---------------- POST USER TASK ---------------- #

    def test_create_task_for_user(self):
        res = self.send_get("/tasks")
        user_id = res.json()["tasks"][0]["assigned_user_ids"][0]

        payload = {"name": "New Task", "status": "new"}
        res = self.send_post(f"/user_tasks/{user_id}", payload)

        self.assertEqual(200, res.status_code)
        data = res.json()

        created_task_id = data["task_id"]

        # VERIFY correct assignment
        res = self.send_get(f"/user_tasks/{user_id}")
        task_ids = [t["task_id"] for t in res.json()["tasks"]]

        self.assertIn(created_task_id, task_ids)

    # ---------------- MUTATION KILLERS ---------------- #

    def test_create_task_without_name(self):
        res = self.send_get("/tasks")
        user_id = res.json()["tasks"][0]["assigned_user_ids"][0]

        payload = {"status": "new"}  # missing name

        res = self.send_post(f"/user_tasks/{user_id}", payload)
        data = res.json()

        self.assertNotEqual(200, res.status_code)
        self.assertTrue("error" in data or "message" in data)

    def test_create_task_invalid_user(self):
        payload = {"name": "Test Task", "status": "new"}

        res = self.send_post("/user_tasks/invalid_user", payload)
        data = res.json()

        self.assertNotEqual(200, res.status_code)
        self.assertTrue("error" in data or "message" in data)


if __name__ == "__main__":
    unittest.main()