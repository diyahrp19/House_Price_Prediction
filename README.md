# House_Price_Prediction

A simple machine learning project to predict house prices based on house size.  
It provides both a Flask API for programmatic predictions and a Streamlit web app for interactive use.

## Files
- `train_model.py`  – trains the Linear Regression model
- `app.py`          – Flask API for predictions
- `app_ui.py`       – Streamlit user interface

## Run
```bash
# Train the model
python train_model.py

# Start Flask API
python app.py

# Start Streamlit UI
streamlit run app_ui.py
