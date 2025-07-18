import time

import requests  # Needs requests module installed: pip install requests -U
from pypresence import Presence
import api.api as api

CLIENT_ID = '1395545885349515274'  # Your client ID here

"""
You need to upload your image(s) here:
https://discord.com/developers/applications/<APP ID>/rich-presence/assets
"""

def get_presence_data():
    try:
        rank = api.main()
        rank_name, rank_val = rank.split(' ')
        image = rank_name.lower() + "-" + rank_val.lower() + ".png"
        image = "static/"+ image

        return {'state': "Peak Rank: " + rank, 'small_image':image}
    except Exception:
        # update failed data
        return {'state': 'Error!'}


def run():
    presence = Presence(CLIENT_ID)
    presence.connect()
    while True:
        data = get_presence_data()
        presence.update(**data)
        time.sleep(15)


if __name__ in '__main__':
    run()
