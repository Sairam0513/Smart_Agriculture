from fastapi import FastAPI
import uvicorn
from env import SmartAgriEnv

app = FastAPI()
env = SmartAgriEnv()

@app.post("/reset")
def reset():
    obs = env.reset()
    return {"observation": obs}

@app.post("/step")
def step(action: dict):
    obs, reward, done, info = env.step(action)
    return {
        "observation": obs,
        "reward": reward,
        "done": done,
        "info": info
    }

@app.get("/state")
def state():
    return {"state": env.state()}

@app.get("/")
def home():
    return {"message": "Smart Agriculture OpenEnv is running"}

# ✅ REQUIRED MAIN FUNCTION
def main():
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)

# ✅ REQUIRED ENTRY POINT
if __name__ == "__main__":
    main()
