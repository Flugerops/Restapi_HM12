from flask import Flask, render_template, request, url_for, flash, redirect
from requests import get, Response
from os import getenv

app = Flask(__name__)

BACKEND_URL = getenv("BACKEND_URL")

@app.get("/")
def index():
    return render_template("index.html")



@app.get("/random")
@app.get("/random/<int:random_max>")
def random_get(random_max:int=100):
    response = get(f"{BACKEND_URL}/random/{random_max}")
    if response.status_code == 200:
        context = {"context": str(response.json())}
        print(context)
        return render_template("index.html", **context)
    return(f"Error {response.status_code}")

@app.get("/current_date")
def current_date():
    response = get(f"{BACKEND_URL}/current_date")
    if response.status_code == 200:
        context = {"context": response.json()}
        return render_template("index.html", **context)
    return(f"Error {response.status_code}")
        
@app.get("/weather/<city>")
def get_weather(city:str):
    response = get(f"{BACKEND_URL}/weather/{city}")
    if response.status_code == 200:
        context = {"context": response.json()}
        return render_template("weather.html", **context)
    return(f"Error {response.status_code}")