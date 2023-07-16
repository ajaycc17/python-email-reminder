import os
import html
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()


# 1 - facts api
def fetch_facts():
    url = "https://facts-by-api-ninjas.p.rapidapi.com/v1/facts"
    headers = {
        "X-RapidAPI-Key": os.environ["rapid_api_key_1"],
        "X-RapidAPI-Host": "facts-by-api-ninjas.p.rapidapi.com",
    }
    response = requests.request("GET", url, headers=headers)
    topic = "Curious facts"
    return topic, response.json()[0]["fact"]


# 2 - jokes api_1
def fetch_jokes():
    url = "https://jokes-by-api-ninjas.p.rapidapi.com/v1/jokes"
    headers = {
        "X-RapidAPI-Key": os.environ["rapid_api_key_1"],
        "X-RapidAPI-Host": "jokes-by-api-ninjas.p.rapidapi.com",
    }
    response = requests.request("GET", url, headers=headers)
    topic = "Smile please"
    return topic, response.json()[0]["joke"]


# 3 - jokes api_2
def fetch_jokes2():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.request("GET", url)
    topic = "Maybe a reason to laugh"
    return topic, response.json()["setup"] + "\n" + response.json()["punchline"]


# 4 - dad jokes
def fetch_dadjoke():
    url = "https://dad-jokes-by-api-ninjas.p.rapidapi.com/v1/dadjokes"
    headers = {
        "X-RapidAPI-Key": os.environ["rapid_api_key_1"],
        "X-RapidAPI-Host": "dad-jokes-by-api-ninjas.p.rapidapi.com",
    }
    response = requests.request("GET", url, headers=headers)
    topic = "Dad joke"
    return topic, response.json()[0]["joke"]


# 5 - cat facts
def cat_fact():
    url = "https://catfact.ninja/fact"
    cat = requests.request("GET", url)
    topic = "Fact about a ninja cat"
    return topic, cat.json()["fact"]


# 6 - chuck norris jokes
def chuck_norris():
    url = "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random"
    headers = {
        "accept": "application/json",
        "X-RapidAPI-Key": os.environ["rapid_api_key_2"],
        "X-RapidAPI-Host": "matchilling-chuck-norris-jokes-v1.p.rapidapi.com",
    }
    response = requests.get(url, headers=headers)
    topic = "Chuck Norris says"
    return topic, response.json()["value"]


# 7 - open trivia
def open_trivia():
    url = "https://opentdb.com/api.php?amount=1"
    response = requests.get(url)
    topic = "Knowledge check"
    return topic, html.unescape(
        response.json()["results"][0]["question"]
    ) + "\nAnswer: " + html.unescape(response.json()["results"][0]["correct_answer"])


# 8 - today's date facts
def date_facts():
    currentDay = datetime.now().day
    currentMonth = datetime.now().month
    url = f"http://numbersapi.com/{currentMonth}/{currentDay}/date"
    response = requests.get(url)
    topic = "Today is a special day"
    return topic, response.text


# 9 - random date facts
def random_date_facts():
    url = "http://numbersapi.com/random/date"
    response = requests.get(url)
    topic = "Any random day is a special day"
    return topic, response.text
