# Housing Price Prediction — Streamlit Web App

[![Live Demo](https://img.shields.io/badge/Live%20App-Streamlit-FF4B4B?logo=streamlit)](https://house-predicti.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://python.org)
[![Model](https://img.shields.io/badge/Model-Linear%20Regression-green)](https://scikit-learn.org)

> A beginner-friendly end-to-end machine learning project that predicts house prices based on area (sq.ft) using Linear Regression, with an interactive Streamlit web app for real-time predictions.

**[Try the Live App →](https://house-predicti.streamlit.app/)**

---

## What It Does

Enter a house area in square feet → the app instantly predicts the estimated price in ₹ using a trained Linear Regression model.

---

## Project Structure

```
housing-price-prediction-streamlit-app/
│
├── app.py           ← Streamlit web app (prediction interface)
├── train.py         ← Model training, evaluation & visualization
├── house.csv        ← Dataset (area vs price)
├── model.pkl        ← Saved trained Linear Regression model
├── requirements.txt ← Python dependencies
└── README.md
```

> **Note for contributors:** `train.py` references `data/house.csv` and `app.py` references `model/model.pkl` internally — both files actually live at the **root level**. If running locally, either update the paths in the scripts or create `data/` and `model/` subdirectories and move the files there accordingly.

---

## How It Works

### Step 1 — Model Training (`train.py`)

Loads `house.csv` which contains two columns — `area` (sq.ft) and `price` (₹).

```python
x = df[['area']]   # Feature
y = df[['price']]  # Target
```

- Splits data **80% train / 20% test** (`random_state=42`)
- Trains a `LinearRegression` model from scikit-learn
- Evaluates performance using **R² score** and **Mean Squared Error (MSE)**
- Plots actual data (blue scatter) vs fitted regression line (red) for visual validation
- Saves the trained model to `model.pkl` using `joblib`

### Step 2 — Streamlit App (`app.py`)

- Loads the saved `model.pkl` at startup
- Accepts area input between **500 – 20,000 sq.ft**
- On clicking **"Predict Price"**, runs inference and displays the result:

```
Predicted House Price: ₹XX,XXX.XX
```

---

## Model Performance

| Metric | Value |
|---|---|
| Algorithm | Linear Regression |
| Feature | Area (sq.ft) |
| Target | Price (₹) |
| Train / Test Split | 80% / 20% |
| R² Score | *(run `python train.py` to see)* |
| MSE | *(run `python train.py` to see)* |

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| Pandas & NumPy | Data loading and processing |
| Scikit-learn | Linear Regression model |
| Matplotlib | Regression line visualization |
| Joblib | Model serialization |
| Streamlit | Web app interface |

---

## How to Run Locally

### 1. Clone the repo
```bash
git clone https://github.com/KrishnaJ4F/housing-price-prediction-streamlit-app.git
cd housing-price-prediction-streamlit-app
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Train the model (optional — `model.pkl` already included)
```bash
python train.py
```

### 4. Launch the app
```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501`

---

## Requirements

```
streamlit
scikit-learn
pandas
numpy
matplotlib
joblib
```

---

## Key Insights

- Area is a strong single predictor of house price — the linear relationship holds well for standard residential properties
- The regression line visualization in `train.py` clearly shows the positive price-area trend
- Separating `train.py` (model training) and `app.py` (model serving) is good ML engineering practice — training and inference are fully decoupled

---

## Author

**Krishna Kumar** — [@KrishnaJ4F](https://github.com/KrishnaJ4F)
