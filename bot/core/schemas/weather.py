from pydantic import BaseModel




class Main(BaseModel):
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    humidity: int
    

class Wind(BaseModel):
    speed: float
    

class Clouds(BaseModel):
    all: int

class WeatherResponseBase(BaseModel):
    main: Main
    wind: Wind
    clouds: Clouds
    name: str
    
    
    

    
    
    
    