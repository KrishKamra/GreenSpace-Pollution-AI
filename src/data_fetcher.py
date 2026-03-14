import requests

class DataFetcher:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/air_pollution"

    def get_real_pm25(self, lat, lon):
        """
        Fetches current PM2.5 data to 'Verify' our model or gather new training data.
        """
        params = {
            "lat": lat,
            "lon": lon,
            "appid": self.api_key
        }
        response = requests.get(self.base_url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            # Navigate the JSON structure to find PM2.5
            return data['list'][0]['components']['pm2_5']
        else:
            raise Exception(f"API Error: {response.status_code}")