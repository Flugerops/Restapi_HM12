from fastapi import FastAPI
from fastapi.exceptions import HTTPException
import random
from datetime import datetime
from dotenv import load_dotenv
from os import getenv
import requests

load_dotenv()
key = getenv("key")
app = FastAPI()


@app.get("/")
def index():
    return {"Hello": "Dmytro", "5 stars": "pls"}


@app.get("/random")
@app.get("/random/{random_max}")
def random_get(random_max:int=100):
    if not random_max <= 0:
        return random.randint(1, random_max)
    else:
        raise HTTPException(status_code=400, detail="Invalid Argument")

@app.get("/current_date")
def current_date():
    return datetime.now().strftime("%d.%m.%y")


@app.get("/weather/{city}")
def get_weater(city:str):
    try: 
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric").json()
        weather_data = {
            "temperature": response.get('main').get('temp'),
            "humidity": response.get('main').get("humidity"),
            "wind_speed": response.get("wind").get("speed"),
        }
        return weather_data
    except:
        raise HTTPException(status_code=400, detail='Invalid Argument')      
