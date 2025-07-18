import time
import psutil
from pypresence import Presence
import api.api as api

CLIENT_ID = '1395545885349515274'

RPC = Presence(client_id=CLIENT_ID)
RPC.connect()

def is_valorant_running():
    for proc in psutil.process_iter(['name']):
        try:
            if proc.info['name'] and "valorant" in proc.info['name'].lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    return False

def get_presence_data():
    try:
        if not is_valorant_running():
            return None  # ⛔ Don't show anything if Valorant is not running

        rank = api.main()  # z.B. "Gold 3"
        if not rank:
            raise ValueError("No rank returned")

        if rank == "Radiant":
            image = "radiant"
        else:
            rank_name, rank_val = rank.split(' ')
            image = rank_name.lower() + "-" + rank_val.lower()

        return {
            'state': "In-Game",
            'details': f"Peak Rank: {rank}",
            'large_image': "valorant-logo",  # Make sure this is uploaded
            'large_text': "VALORANT",
            'small_image': image
        }

    except Exception as e:
        print(f"[ERROR] {e}")
        return {
            'state': 'Error!',
            'small_image': 'error',
            'small_text': "Something went wrong"
        }

def run():
    while True:
        data = get_presence_data()

        if data:
            RPC.update(**data)
        else:
            RPC.clear()  # ❌ Clears Rich Presence when Valorant isn’t running

        time.sleep(15)

if __name__ == '__main__':
    run()
