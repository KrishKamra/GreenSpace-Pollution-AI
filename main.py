import os
from dotenv import load_dotenv
from src.model_utility import PollutionPredictor
from src.data_fetcher import DataFetcher

# 1. SETUP: Load environment variables and initialize components
load_dotenv() 
API_KEY = os.getenv("OPENWEATHER_API_KEY")

# Initialize the pre-trained model from the src folder
predictor = PollutionPredictor(model_path='src/trained_model.pkl')

# Initialize the data gatherer
fetcher = DataFetcher(api_key=API_KEY)

def run_app():
    print("--- Urban GreenSpace Pollution Predictor ---")
    
    try:
        # 2. INPUT: Get coordinates from user
        lat = float(input("Enter Latitude: "))
        lon = float(input("Enter Longitude: "))
        
        # 3. FETCH: Get real-time ground truth for comparison
        print(f"\nFetching real-time data for ({lat}, {lon})...")
        real_pm25 = fetcher.get_real_pm25(lat, lon)
        
        # 4. SIMULATION: For this project, we manually input local features
        green = float(input("Enter Green Index (%) for this area: "))
        dist = float(input("Enter Distance to nearest Industry (km): "))
        
        # 5. PREDICT: Run the model
        prediction = predictor.predict_pm25(green, dist)
        
        # 6. OUTPUT: Compare results
        print("\n" + "="*30)
        print(f"Current Measured PM2.5: {real_pm25} ug/m3")
        print(f"Model's Predicted PM2.5: {prediction} ug/m3")
        print("="*30)
        
        # Logic: Calculate the 'Residual' of our real-time test
        error = round(abs(real_pm25 - prediction), 2)
        print(f"Model Variance: {error} units")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_app()