from pypresence import Presence
import time

"""
You need to upload your image(s) here:
https://discord.com/developers/applications/<APP ID>/rich-presence/assets
"""

client_id = "1395545885349515274"  # Enter your Application ID here.
RPC = Presence(client_id=client_id)
RPC.connect()

# Make sure you are using the same name that you used when uploading the image
RPC.update(large_image="big-image", large_text="Large Text Here!",
            small_image="small-image", small_text="Small Text Here!")

while 1:
    time.sleep(15) #Can only update presence every 15 seconds
