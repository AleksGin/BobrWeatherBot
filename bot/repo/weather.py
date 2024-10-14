from aiohttp import ClientSession
from core.schemas import WeatherResponseBase


class WeatherRepo:
    def __init__(self, http_session: ClientSession, api_key: str, url: str) -> None:
        self.http_session = http_session
        self.api_key = api_key
        self.url = url

    async def get_weather_info_by_id(self, city_name: str):
        params = {
            "q": city_name,
            "appid": self.api_key,
            "units": "metric", 
            "lang": "ru"
        }

        url = self.url + f"?q={city_name}&appid={self.api_key}"

        async with self.http_session.get(url=url, params=params) as resp:
            return WeatherResponseBase(**await resp.json())
