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
    
    #power in kWh
    fan_energy = (appliance_power["Fan"] * fan_hours) / 1000
    light_energy = (appliance_power["Light"] * light_hours) / 1000
    laptop_energy = (appliance_power["Laptop"] * laptop_hours) / 1000
    charger_energy = (appliance_power["Charger"] * charger_hours) / 1000
    cooler_energy = (appliance_power["Cooler"] * cooler_hours) / 1000
    iron_energy = (appliance_power["Iron"] * iron_hours) / 1000

    total_energy = ( fan_energy + light_energy + laptop_energy + charger_energy + cooler_energy + iron_energy)

    data.append([
        current_date.date(),
        temperature,
        occupancy,
        fan_hours,
        light_hours,
        laptop_hours,
        charger_hours,
        cooler_hours,
        iron_hours,
        total_energy
    ])
#dataframe
df = pd.DataFrame(
    data,
    columns=[
        "Date",
        "Temperature_C",
        "Occupancy",
        "Fan_Hours",
        "Light_Hours",
        "Laptop_Hours",
        "Charger_Hours",
        "Cooler_Hours",
        "Iron_Hours",
        "Energy_kWh"
    ]
)

print(df.head())

df.to_csv("dataset/energy_data.csv", index=False)

print("Dataset saved successfully!")