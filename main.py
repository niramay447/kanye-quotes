import requests
from tkinter import *

def get_quote():
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]


window = Tk()
window.title("Kanye says...")
window.config(pady=50, padx=50)

canvsa