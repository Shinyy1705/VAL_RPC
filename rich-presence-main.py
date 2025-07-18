import time
from pypresence import Presence
import api.api as api

CLIENT_ID = '1395545885349515274'

RPC = Presence(client_id=CLIENT_ID)
RPC.connect()

def get_presence_data():
    try:
        rank = api.main()  # z.B. "Gold 3"
        if rank == "Radiant":
            image = "radiant"
        else:
            rank_name, rank_val = rank.split(' ')
            image = rank_name.lower() + "-" + rank_val.lower()


        return {
            'state': "Peak Rank: " + rank,
            'small_image': image
        }
    except Exception as e:
        print(f"[ERROR] {e}")
        return {
            'state': 'Error!',
            'small_image': 'error',  # Optional: Fallback-Bild
            'small_text': "Something went wrong"
        }

def run():
    while True:
        data = get_presence_data()
        RPC.update(**data)
        time.sleep(15)

if __name__ == '__main__':
    run()