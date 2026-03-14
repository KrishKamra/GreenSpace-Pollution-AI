import joblib
import pandas as pd
import numpy as np

class PollutionPredictor:
    def __init__(self, model_path):
        try:
            self.loaded_model = joblib.load(model_path)
        except FileNotFoundError:
            raise FileNotFoundError(f"Could not find the model file at: {model_path}")

    def predict_pm25(self, green_index, industry_dist):
        if not (0 <= green_index <= 100) or industry_dist < 0:
            raise ValueError("Invalid Input: Check your ranges.")

        input_data = pd.DataFrame({
            'const': [1.0],
            'Green_Index': [green_index],
            'Industry_Dist': [industry_dist],
            'Green_x_Dist': [green_index * industry_dist]
        })

        prediction = self.loaded_model.predict(input_data)[0]
        
        return max(0, round(prediction, 2))

if __name__ == "__main__":
    try:
        my_model = PollutionPredictor(model_path='src/trained_model.pkl')
        estimate = my_model.predict_pm25(green_index=45, industry_dist=2.5)
        print(f"Test prediction: {estimate}")
    except Exception as e:
        print(f"Test failed: {e}")