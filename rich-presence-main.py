import os
import time
import psutil
from pypresence import Presence
import api.api as api  # Your custom module to get rank info

# Replace with your actual Discord application client ID
CLIENT_ID = os.getenv("CLIENTID")  # Replace with your actual client ID

# Connect to Discord Rich Presence
RPC = Presence(client_id=CLIENT_ID)
RPC.connect()

# Check if Valorant is currently running
def is_valorant_running():
    for proc in psutil.process_iter(['name']):
        try:
            #edit valorant to discord for testing purposes
            if proc.info['name'] and "discord" in proc.info['name'].lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    return False

# Build the presence data
def get_presence_data():
    try:
        # Only show presence if Valorant is running
        if not is_valorant_running():
            return None

        # Get peak rank from your API (e.g., "Gold 3")
        rank = api.main()
        if not rank:
            raise ValueError("No rank returned from API")

        # Prepare small image key based on rank
        if rank.lower() == "radiant":
            image = "radiant"
        else:
            rank_name, rank_val = rank.split(" ", 1)
            image = f"{rank_name.lower()}-{rank_val.lower()}"

        # Return the full presence data with a button
        return {
            'state': "Coaching Valorant",
            'details': f"Peak Rank: {rank}",
            'large_image': "valorant-logo",  # Make sure this image is uploaded in Dev Portal
            'large_text': "VALORANT",
            'small_image': image,
            'small_text': f"{rank}",
            'buttons': [
                {
                    "label": "Join Discord",
                    "url": os.getenv("BUTTONLINK")  # Must start with https://
                }
            ]
        }

    except Exception as e:
        print(f"[ERROR] {e}")
        return {
            'state': "Error!",
            'details': "Could not fetch rank",
            'large_image': "valorant-logo",
            'small_image': "error",
            'small_text': "Something went wrong"
        }

# Main loop to update presence
def run():
    while True:
        presence = get_presence_data()

        if presence:
            RPC.update(**presence)
        else:
            RPC.clear()  # Clear presence when Valorant is not running

        time.sleep(15)

if __name__ == '__main__':
    run()
