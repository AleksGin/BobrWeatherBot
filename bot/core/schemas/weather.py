from pydantic import BaseModel



class WeatherResponseBase(BaseModel):
    id: int
    name: str
    

    
    
    
    