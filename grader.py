def grade(task, action):
    correct = task["answer"]

    if action == correct:
        return 1.0
    elif action in ["water", "fertilize", "pesticide"]:
        return 0.5
    else:
        return -0.5
