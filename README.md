# Smart Hostel Energy Optimization Dashboard

This project predicts the daily energy consumption of a hostel room based on appliance usage and environmental conditions. It also provides suggestions to help reduce unnecessary electricity usage.

The dashboard takes inputs such as temperature, occupancy, and usage hours of appliances like fans, lights, laptops, chargers, coolers, and iron. Using these inputs, the system estimates daily energy consumption in kWh and calculates approximate electricity cost.

Along with prediction, the system also provides optimization recommendations such as reducing cooler usage or improving ventilation to improve energy efficiency.

## Features

* Predicts daily energy consumption using machine learning
* Estimates daily and monthly electricity cost
* Provides energy-saving recommendations
* Visualizes historical energy usage through graphs
* Interactive dashboard built using Streamlit

## Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib / Seaborn
* Streamlit

## Machine Learning Model

Linear Regression is used to predict energy consumption.

Model Performance:

* R² Score: 0.988
* MAE: 0.099
* RMSE: 0.113

## Workflow

1. Generate synthetic energy consumption dataset
2. Perform exploratory data analysis
3. Train machine learning model
4. Generate optimization recommendations
5. Display results on interactive dashboard

## Project Structure

```bash id="1"
energy-dashboard/
│
├── dataset/
│   └── energy_data.csv
├── app.py
├── model.py
├── utils.py
├── generate_data.py
├── eda.py
├── train_model.py
└── requirements.txt
```

## Installation

Install dependencies:

```bash id="2"
pip install -r requirements.txt
```

Run the dashboard:

```bash id="3"
streamlit run app.py
```

## Future Improvements

* Train on real-world energy data
* Use advanced machine learning models
* Deploy dashboard online
* Improve UI and analytics

