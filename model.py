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


st.title("AI Energy Consumption Dashboard")
st.write("Smart Hostel Energy Optimization System")

st.sidebar.header("Input Parameters")

temperature = st.sidebar.slider("Temperature (°C)", 24, 42, 32)
occupancy = st.sidebar.selectbox("Occupancy", [0, 1, 2])
fan_hours = st.sidebar.slider("Fan Hours", 0, 24, 8)
light_hours = st.sidebar.slider("Light Hours", 0, 24, 5)
laptop_hours = st.sidebar.slider("Laptop Hours", 0, 24, 4)
charger_hours = st.sidebar.slider("Charger Hours", 0, 24, 2)
cooler_hours = st.sidebar.slider("Cooler Hours", 0, 24, 0)
iron_hours = st.sidebar.slider("Iron Hours", 0, 2, 0)

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

    st.metric("Predicted Energy Consumption", f"{prediction:.2f} kWh")

    daily_cost = prediction * 8
    monthly_cost = daily_cost * 30

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Daily Cost", f"₹{daily_cost:.2f}")

    with col2:
        st.metric("Monthly Cost", f"₹{monthly_cost:.0f}")

    if prediction > 3.5:
        st.error("High energy consumption detected!")
    elif prediction > 2:
        st.warning("Moderate energy consumption")
    else:
        st.success("Efficient energy usage")

    recommendations = get_recommendations(
        temperature,
        fan_hours,
        cooler_hours
    )

    st.subheader("Optimization Recommendations")

    for rec in recommendations:
        st.write("•", rec)

    chart_data = df.set_index("Date")

    st.subheader("Historical Energy Usage")
    st.line_chart(chart_data["Energy_kWh"])