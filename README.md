# VoltPredict – Electricity Price Prediction using Machine Learning

## Overview

VoltPredict is a machine learning-powered web application developed to predict electricity prices based on operational, environmental, and market-related factors. Accurate electricity price forecasting helps energy providers, industries, and consumers make informed decisions regarding energy consumption and resource planning.

The project combines Machine Learning and Django to provide a user-friendly interface where users can enter relevant parameters and receive predicted electricity prices in real time.

---

## Problem Statement

Electricity demand is continuously increasing due to the widespread use of electronic devices, industrial machinery, electric vehicles, and digital infrastructure. Electricity prices fluctuate based on several factors such as energy production, weather conditions, system load, and environmental conditions.

This project aims to predict electricity prices using historical energy market data and machine learning techniques.

---

## Key Features

- Machine Learning-based electricity price prediction
- Data preprocessing and feature engineering
- Real-time prediction through a Django web application
- User-friendly interface for entering energy-related parameters
- Integration of trained ML model with web deployment

---

## Machine Learning Pipeline

### Data Preprocessing

The dataset was cleaned and prepared using Pandas and NumPy.

Steps performed:

- Handled missing values
- Converted data types to numerical format
- Processed date and time information
- Extracted time-based features such as hour, day, and month
- Removed unnecessary columns

### Feature Engineering

The following features are used by the model:

| Feature                  | Description                                         |
| ------------------------ | --------------------------------------------------- |
| Holiday Flag (0/1)       | Indicates whether the day is a holiday              |
| Forecast Wind Production | Expected wind energy generation                     |
| System Load EA           | Estimated electricity demand/load                   |
| SMPEA                    | Historical electricity market price indicator       |
| Temperature              | Ambient temperature affecting energy consumption    |
| Wind Speed               | Wind conditions affecting renewable generation      |
| CO2 Intensity            | Carbon emission intensity of electricity production |
| Actual Wind Production   | Actual wind energy generated                        |
| System Load EP2          | Electricity demand measurement                      |
| Hour                     | Hour of the day (0–23)                              |
| Day                      | Day of the month                                    |
| Month                    | Month of the year                                   |

### Target Variable

**SMPEP2**

The model predicts SMPEP2, which represents the electricity market price.

---

## Model Development

### Algorithm Used

**Random Forest Regressor**

Random Forest Regression was selected because:

- It handles non-linear relationships effectively.
- It works well with mixed energy and environmental data.
- It reduces overfitting by combining multiple decision trees.
- It provides stable and reliable predictions.

### Training Process

1. Dataset loaded using Pandas.
2. Missing values cleaned.
3. Date and time features extracted.
4. Features and target variable separated.
5. Dataset split into training and testing sets.
6. Random Forest Regression model trained.
7. Trained model serialized using Pickle.

---

## Technology Stack

### Machine Learning

- Python
- Pandas
- NumPy
- Scikit-learn
- Pickle

### Web Development

- Django
- HTML
- CSS

---

## Project Workflow

1. User enters electricity-related parameters.
2. Django backend receives the inputs.
3. Trained machine learning model processes the data.
4. Model predicts the electricity price.
5. Predicted result is displayed on the web interface.

---

## Installation & Setup

### Clone the Repository

```bash
git clone https://github.com/Kavyasrimedi/electricity-price-prediction.git
cd electricity-price-prediction
```

### Install Dependencies

```bash
pip install django pandas numpy scikit-learn
```

### Train the Model

```bash
python train_model.py
```

### Run the Application

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

## Future Enhancements

- Integration of real-time electricity market data
- Advanced forecasting using XGBoost and Gradient Boosting
- Time-series forecasting models such as LSTM
- Interactive dashboards and analytics
- Cloud deployment for large-scale access

---

## Author

**Kavya Sri**

Machine Learning | AI & Data Science | Full Stack Enthusiast
