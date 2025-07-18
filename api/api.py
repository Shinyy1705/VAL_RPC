import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

#PEAK RANK Ohne RR
#IN LOBBY / IN QUEUE
#

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

get_account_rank('snedx', 'valo')

def get_account_peak_rank(puuid):
    url = f"https://api.henrikdev.xyz/valorant/v3/by-puuid/mmr/EU/PC/{puuid}"
    headers = {
        'Authorization': API_KEY
    }
    response = requests.get(url, headers=headers)
    return response.json()

def get_puudi(name, tag):
    url = f"https://api.henrikdev.xyz/valorant/v1/account/{name}/{tag}"
    headers = {
        'Authorization': API_KEY
    }
    response = requests.get(url, headers=headers)
    acc_data = response.json()
    puuid = acc_data['data']['puuid']
    return puuid

def main():

    puuid = get_puudi("snedx", "valo")
    rank = get_account_peak_rank(puuid)
    rank = rank.get("data")
    rank = rank.get("peak")
    rank = rank.get("tier")
    rank = rank.get("name")
    return rank

def image():
    rank = get_account_rank('snedx', 'valo')
    rank = rank.get("data")
    rank = rank[0]
    rank = rank.get("images")
    image = rank.get("small")
    return image



