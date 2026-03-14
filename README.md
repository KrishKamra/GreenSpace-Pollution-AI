# 🌿 GreenSpace-Pollution-AI: Urban Planning Analytics

An industry-grade **Multiple Linear Regression** project that quantifies the impact of urban greenery on air quality ($PM_{2.5}$), accounting for industrial proximity and variable interactions.

## 🚀 The Core Objective

This project moves beyond simple correlation to answer a specific urban planning question: **"How does the effectiveness of urban green spaces change based on their distance from industrial emission sources?"**

By leveraging **Ordinary Least Squares (OLS)**, this model identifies non-linear synergies between environmental factors, providing a prescriptive tool for city planners.

---

## 🛠️ Technical Architecture

The project is built with a modular, production-ready structure:

* **`src/model_utility.py`**: Encapsulated `PollutionPredictor` class with model serialization and input validation.
* **`src/data_fetcher.py`**: API integration with OpenWeatherMap for real-time air quality verification.
* **`main.py`**: The orchestration layer connecting real-world data with predictive analytics.
* **`EDA/`**: Jupyter notebooks detailing the statistical "discovery" phase (Residual analysis, P-value testing, and Multicollinearity checks).

---

## 📊 Mathematical Intuition & Insights

### 1. The Interaction Effect

Unlike a standard linear model, this project implements an **interaction term** ($Green \times Distance$).

* **Finding**: We discovered that greenery has a higher marginal benefit when located in close proximity to industrial zones.
* **Equation**: $y = \beta_0 + \beta_1(\text{Green}) + \beta_2(\text{Dist}) + \beta_3(\text{Green} \cdot \text{Dist}) + \epsilon$

### 2. Statistical Validation

* **R-Squared**: $0.99+$ (Synthetic baseline) / High explanatory power.
* **P-Value Testing**: All features were tested for significance at the $\alpha = 0.05$ level.
* **Residual Analysis**: Homoscedasticity was confirmed via residual plotting to ensure no systematic bias in predictions.

---

## 💻 Setup & Usage

### 1. Environment Setup

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1  # Windows
pip install -r requirements.txt

```

### 2. API Configuration

Create a `.env` file in the root directory:

```text
OPENWEATHER_API_KEY=your_key_here

```

### 3. Running the Predictor

```bash
python main.py

```

---

## 🔮 Future Scope

* **Satellite Integration**: Automating the `Green_Index` calculation using **Google Earth Engine (GEE)** to pull NDVI values directly from Sentinel-2 satellite imagery.
* **Spatial Interpolation**: Moving from linear regression to **Geographically Weighted Regression (GWR)** to account for regional climate variations.

---

## 👨‍🔬 Author

**Krish Kamra**
