from requests import Session
from colorama import init
from vardxg import Colors, Write, Center
import os
request = Session()

init(autoreset=True), os.system('cls')

send = 0

def banner():
    logo = ("""
    ███╗   ██╗ ██████╗ ██╗         ██████╗ ██╗███████╗
    ████╗  ██║██╔════╝ ██║         ██╔══██╗██║██╔════╝
    ██╔██╗ ██║██║  ███╗██║         ██║  ██║██║█████╗   # Made by @vardxg <3
    ██║╚██╗██║██║   ██║██║         ██║  ██║██║██╔══╝  
    ██║ ╚████║╚██████╔╝███████╗    ██████╔╝██║███████╗
    ╚═╝  ╚═══╝ ╚═════╝ ╚══════╝    ╚═════╝ ╚═╝╚══════╝

    """)
    Write.Print(Center.XCenter(logo), Colors.red, interval=0)
    return logo

ngl = banner()

username = input("\n [?] Enter Target Username >>> ")

class vardxg():
    def sendTell():
        global send, fail
        with open('messages.txt', 'r') as f:
            messages = f.read().splitlines()
        
        for message in messages:
            try:
                url = "https://ngl.link/api/submit"

                headers = {
                    "accept": "*/*",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
                    "connection": "keep-alive",
                    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "cookie": "mp_e8e1a30fe6d7dacfa1353b45d6093a00_mixpanel=%7B%22distinct_id%22%3A%20%22%24device%3A18830db692a66c-0be6a32a7ad825-26031a51-1940bf-18830db692a66c%22%2C%22%24device_id%22%3A%20%2218830db692a66c-0be6a32a7ad825-26031a51-1940bf-18830db692a66c%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D; _ga_5DV1ZR5ZHG=GS1.1.1684446866.1.0.1684446866.0.0.0; _ga=GA1.1.1133102881.1684446866; __stripe_mid=9bbe76e3-4db4-4a07-b105-595434b6b928883683; __stripe_sid=0e77d0b3-4fb0-45dc-9136-2951d73278534c7105",
                    "host": "ngl.link",
                    "origin": "https://ngl.link",
                    "referer": "https://ngl.link/qo4cy",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
                }

                payload = {
                    "username": username,
                    "question": message,
                    "deviceId": "6eac9603-576b-4461-a07c-0e632e9f57f6",
                    "gameSlug": "",
                    "referrer": ""
                }

                response = request.post(url ,headers=headers, data=payload).json()['questionId']

                send += 1
                os.system('cls')
                Write.Print(f"\n [!] Send >>> {send} | Tell >>> {message} | Tell ID >>> {response}", Colors.purple, interval=0)
            
            except Exception as e:
                print(e)
    
    sendTell()
vardxg()
# Made with <3 by @Fhivo! 
