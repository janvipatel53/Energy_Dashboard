import pandas as pd
import random
from datetime import datetime, timedelta

appliance_power = {
    "Fan": 75,
    "Light": 12,
    "Laptop": 65,
    "Charger": 20,
    "Cooler": 200,
    "Iron": 1000
}

data = []
start_date = datetime(2026, 1, 1)

for i in range(365):
    current_date = start_date + timedelta(days=i)

    temperature = random.randint(24, 42)
    occupancy = random.randint(0, 2)

    if temperature < 30:
        fan_hours = random.randint(4, 8)
    elif temperature <= 35:
        fan_hours = random.randint(8, 12)
    else:
        fan_hours = random.randint(12, 18)

    if occupancy == 0:
        light_hours = random.randint(0, 2)
    else:
        light_hours = random.randint(4, 8)

    if occupancy == 0:
        laptop_hours = 0
    else:
        laptop_hours = random.randint(2, 8)

    charger_hours = random.randint(1, 4)

    if temperature < 32:
        cooler_hours = 0
    elif temperature <= 37:
        cooler_hours = random.randint(2, 5)
    else:
        cooler_hours = random.randint(5, 10)

    iron_hours = random.choice([0, 0, 0, 1])