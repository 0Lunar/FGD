import requests
from bs4 import BeautifulSoup as bs
from colorama import Fore
import sys


def download(url: str):
    torrentUrl = ""

    r = requests.get(url).text
    soup = bs(r, 'html.parser')

    for i in soup.find_all('a'):

        if ".torrent" in str(i).split(">")[1].split("<")[0]:

            torrentUrl = i.get('href')
            
            print(f"{Fore.GREEN}\n\nTorrent url: {Fore.YELLOW} {torrentUrl} {Fore.RESET}")

            return torrentUrl

    print("Torrent not found!")
    sys.exit()