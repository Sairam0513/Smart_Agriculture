from env import SmartAgriEnv

def main():
    env = SmartAgriEnv()
    obs = env.reset()

    total_reward = 0
    step_count = 0

    print(f"[START] task=smart_agriculture", flush=True)

    done = False

    while not done:
        data = obs["data"]

        # Rule-based decision
        if "soil_moisture" in data:
            decision = "water" if data["soil_moisture"] < 30 else "none"

        elif "N" in data:
            nutrients = {"N": data["N"], "P": data["P"], "K": data["K"]}
            lowest = min(nutrients, key=nutrients.get)
            decision = "fertilize"

        elif "spots" in data:
            decision = "pesticide" if data["spots"] else "none"

        else:
            decision = "none"

        action = {"decision": decision}

        obs, reward, done, _ = env.step(action)

        step_count += 1
        total_reward += reward

        print(f"[STEP] step={step_count} reward={reward}", flush=True)

    print(f"[END] task=smart_agriculture score={total_reward} steps={step_count}", flush=True)


if __name__ == "__main__":
    main()
