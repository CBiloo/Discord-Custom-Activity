

import requests
import time
import os
from secret import header # Create a secret.py file with header containing your discord authorization token

credit = "Reword By Biloo"
valid = "The entered key is valid so the program has just started"
novalid = "Please check the key you entered"

if not "Reword By Biloo" in credit:
    exit()

print("""
███████╗████████╗ █████╗ ████████╗██╗   ██╗███████╗     ██████╗██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███████╗██████╗     
██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██║   ██║██╔════╝    ██╔════╝██║  ██║██╔══██╗████╗  ██║██╔════╝ ██╔════╝██╔══██╗    
███████╗   ██║   ███████║   ██║   ██║   ██║███████╗    ██║     ███████║███████║██╔██╗ ██║██║  ███╗█████╗  ██████╔╝    
╚════██║   ██║   ██╔══██║   ██║   ██║   ██║╚════██║    ██║     ██╔══██║██╔══██║██║╚██╗██║██║   ██║██╔══╝  ██╔══██╗    
███████║   ██║   ██║  ██║   ██║   ╚██████╔╝███████║    ╚██████╗██║  ██║██║  ██║██║ ╚████║╚██████╔╝███████╗██║  ██║    
╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝     ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝    

Remember to check the activity.txt file and the secret.py file to see if you have configured the file correctly
                                                                                                                   
""")

keyz = input("Please enter your key : ")

if not "keyz:584" in keyz:
    print(novalid)
    exit = input("")
    exit()
else:
    print("")
    print(valid)

payload = {"custom_status":{
    "emoji_name": "", # Status emoji
    "text": ""
}}

endpoint = "https://discord.com/api/v9/users/@me/settings"

def main():
    while True:
        with open("./activity.txt", "r") as r:
            for line in r:
                line = line.rstrip() # Remove blank spaces
                if line == "" : continue # Continue if blank line
                payload["custom_status"]["text"] = line
                r = requests.patch(endpoint, json=payload, headers=header)
                if r.status_code != 200 : break
                time.sleep(0.5) # Interval

def reset(): # Reset status
    payload["custom_status"]["text"], payload["custom_status"]["emoji_name"] = "", ""
    r = requests.patch(endpoint, json=payload, headers=header)

if __name__ == "__main__":
    main()
