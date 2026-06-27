import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("dataset/energy_data.csv")

X = df.drop(columns=["Date", "Energy_kWh"])
y = df["Energy_kWh"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

st.title("AI Energy Consumption Dashboard")

def get_recommendations(temperature, fan_hours, cooler_hours):
    recommendations = []

    if cooler_hours > 7:
        recommendations.append(
            "Reduce cooler usage by 2 hours/day to save energy."
        )

    if fan_hours > 14:
        recommendations.append(
            "Consider reducing fan speed during cooler hours."
        )

    if temperature > 38:
        recommendations.append(
            "Improve ventilation by opening windows in evening."
        )

    if not recommendations:
        recommendations.append("Energy usage is already optimized.")

    return recommendations

st.write("Hostel Energy Optimization System")

temperature = st.slider("Temperature (°C)", 24, 42, 32)
occupancy = st.selectbox("Occupancy", [0, 1, 2])
fan_hours = st.slider("Fan Hours", 0, 24, 8)
light_hours = st.slider("Light Hours", 0, 24, 5)
laptop_hours = st.slider("Laptop Hours", 0, 24, 4)
charger_hours = st.slider("Charger Hours", 0, 24, 2)
cooler_hours = st.slider("Cooler Hours", 0, 24, 0)
iron_hours = st.slider("Iron Hours", 0, 2, 0)

if st.button("Predict Energy Consumption"):
    input_data = pd.DataFrame([[
        temperature,
        occupancy,
        fan_hours,
        light_hours,
        laptop_hours,
        charger_hours,
        cooler_hours,
        iron_hours
    ]], columns=X.columns)

    prediction = model.predict(input_data)[0]

    st.success(f"Predicted Energy Consumption: {prediction:.2f} kWh")

    recommendations = get_recommendations(
        temperature,
        fan_hours,
        cooler_hours
    )

    st.subheader("Optimization Recommendations")

    for rec in recommendations:
        st.write("•", rec)