tasks = [
    # EASY - Irrigation
    {
        "type": "irrigation",
        "data": {"soil_moisture": 20, "temperature": 35},
        "answer": "water"
    },

    # MEDIUM - Fertilizer
    {
        "type": "fertilizer",
        "data": {"N": 10, "P": 5, "K": 8},
        "answer": "fertilize"   # ✅ FIXED
    },

    # HARD - Crop Health
    {
        "type": "crop_health",
        "data": {"leaf_color": "yellow", "spots": True},
        "answer": "pesticide"
    }
]
