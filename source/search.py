import requests
from bs4 import BeautifulSoup as bs
from colorama import Fore


url = "https://fitgirl-repacks.site/?s="    # Official url


def search(name: str):
    games = []

    name = name.lower().replace(" ", "-")

    r = requests.get((url + name)).text
    soup = bs(r, 'html.parser')

    for i in soup.find_all('a'):
        if ("https://fitgirl-repacks.site/" + name) in i.get("href") and i.get("href") not in games and "#" not in i.get("href"):

            games.append(i.get("href"))

    if len(games) == 0:

        print(Fore.RED + "\nNo games found!" + Fore.RESET)

        return 0
    
    else:
        print(Fore.YELLOW + "\n\n------------------------------- GAMES FOUND: -------------------------------\n\n")

        game = -1

        cnt = 1

        print(Fore.GREEN)

        print("[0] exit")

        for i in games:
            print("[" + str(cnt) + "] " + str(i).split("/")[-2].replace("-", " "))

            cnt += 1

        while game < 0 or game > cnt-1:

            try:
                game = int(input(Fore.RED + "\n\n => "))

                if game < 0 or game > cnt-1:
                    print(Fore.RED + "\nInvalid value!")

            except:
                print(Fore.RED + "\nInvalid value!")
        
        if game == 0:

            return game

        return games[game-1]