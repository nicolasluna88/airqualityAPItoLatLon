import json
from pathlib import Path

def loadConfig():
    configPath = Path(__file__).resolve().parents[2] / "config" / "airQuality.json"
    with open(configPath, "r", encoding="utf-8") as f:
        return json.load(f)