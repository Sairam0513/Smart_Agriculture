import os
from openai import OpenAI
from env import SmartAgriEnv

def main():
    # ✅ Use Hackathon LLM Proxy
    client = OpenAI(
        base_url=os.environ["API_BASE_URL"],
        api_key=os.environ["API_KEY"]
    )

    env = SmartAgriEnv()
    obs = env.reset()

    total_reward = 0
    step_count = 0

    print("[START] task=smart_agriculture", flush=True)

    done = False

    while not done:
        data = obs["data"]

        # ✅ LLM CALL (MANDATORY)
        prompt = f"""
        You are an agriculture expert.

        Based on this data:
        {data}

        Choose ONE action:
        water, fertilize, pesticide, none
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",  # proxy will handle routing
            messages=[{"role": "user", "content": prompt}],
        )

        decision = response.choices[0].message.content.strip().lower()

        # fallback safety
        if "water" in decision:
            decision = "water"
        elif "fertilize" in decision:
            decision = "fertilize"
        elif "pesticide" in decision:
            decision = "pesticide"
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
