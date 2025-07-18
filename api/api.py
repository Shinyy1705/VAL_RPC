import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

def get_account_info(name, tag):
    url = f"https://api.henrikdev.xyz/valorant/v1/account/{name}/{tag}"
    headers = {
        'Authorization': API_KEY
    }
    response = requests.get(url, headers=headers)
    return response.json()

def get_account_rank(name, tag):
    url = f"https://api.henrikdev.xyz/valorant/v1/mmr-history/eu/{name}/{tag}"
    headers = {
        'Authorization': API_KEY
    }
    response = requests.get(url, headers=headers)
    return response.json()
