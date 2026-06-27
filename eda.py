import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("dataset/energy_data.csv")

print(df.head())
print(df.shape)
print(df.describe())
print(df.isnull().sum())

#histogram
plt.figure(figsize=(8, 5))
plt.hist(df["Energy_kWh"], bins=20)
plt.xlabel("Energy Consumption (kWh)")
plt.ylabel("Frequency")
plt.title("Distribution of Daily Energy Consumption")
plt.show()

#scatter plot
plt.figure(figsize=(8, 5))
plt.scatter(df["Temperature_C"], df["Energy_kWh"])
plt.xlabel("Temperature (°C)")
plt.ylabel("Energy Consumption (kWh)")
plt.title("Temperature vs Energy Consumption")
plt.show()

correlation = df.drop(columns=["Date"]).corr()
print(correlation["Energy_kWh"])