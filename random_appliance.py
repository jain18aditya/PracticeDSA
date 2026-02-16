"""
Problem: Random Test Execution on Unique Appliances

You are given:
1. A list of hardware appliances (devices).
2. A list of tests that must be executed.

Design a system such that:
- Each test is assigned to exactly one appliance.
- The appliance for each test is chosen randomly.
- No appliance can be selected more than once.
- If there are more tests than appliances, the system should handle it gracefully
  (e.g., stop execution, queue remaining tests, or report insufficient appliances).

Requirements:
- Ensure randomness in appliance selection.
- Ensure one-to-one mapping between tests and appliances (no reuse).
- The solution should be efficient.
- Support sequential or parallel execution (optional).
- Handle edge cases such as empty lists and unequal counts.

Example:
Appliances: [A1, A2, A3, A4]
Tests:      [T1, T2, T3, T4]

Possible Output (random):
T1 → A3
T2 → A1
T3 → A4
T4 → A2

Each appliance is used at most once.

Approach:
- Shuffle the list of appliances randomly.
- Assign each test to the next available appliance.
- Stop when either tests or appliances are exhausted.
"""


import random


class Appliance:
    def __init__(self, id):
        self.id = id

    def run_test(self, test):
        print(f"Running {test.name} on Appliance: {self.id}")


class Test:
    def __init__(self, name):
        self.name = name


class TestScheduler:
    def __init__(self, appliances, tests):
        self.appliances = appliances
        self.tests = tests

    def run(self):
        if len(self.tests) > len(self.appliances):
            print("Not enough appliances for all tests")
            return

        # Randomize appliances (ensures each used once)
        shuffled_appliances = self.appliances[:]
        random.shuffle(shuffled_appliances)

        for test, appliance in zip(self.tests, shuffled_appliances):
            appliance.run_test(test)


# ---------- Example ----------

appliances = [Appliance(i) for i in range(1, 6)]
tests = [
    Test("CPU Test"),
    Test("Memory Test"),
    Test("Disk Test"),
    Test("Network Test"),
    Test("GPU Test")
]

scheduler = TestScheduler(appliances, tests)
scheduler.run()
