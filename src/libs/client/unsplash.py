from src.configuration.apiconfig import ApiConfig
import requests


class Unsplash:
    def __init__(self):
        self.client_id = ApiConfig.client_id
        self.count = ApiConfig.count
        self.query = ApiConfig.query
        self.orientation = ApiConfig.orientation
        self.url = ApiConfig.url

    def get_images(
        self, client_id, count: int, query: str, orientation: str, url: str
    ):
        params = {
            "client_id": client_id,
            "count": count,
            "query": query,
            "orientation": orientation,
        }
        response = requests.get(url, params=params)
        return response
