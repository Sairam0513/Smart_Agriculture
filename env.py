from tasks import tasks
from grader import grade

class SmartAgriEnv:
    def __init__(self):
        self.index = 0

    def reset(self):
        self.index = 0
        return tasks[self.index]

    def step(self, action):
        task = tasks[self.index]

        reward = grade(task, action["decision"])

        self.index += 1
        done = self.index >= len(tasks)

        next_obs = tasks[self.index] if not done else None

        return next_obs, reward, done, {}

    def state(self):
        return tasks[self.index]
