import requests, os
from colorama import Fore
from source import search, banner, getTorrent


def clean():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")



if __name__ == "__main__":

    clean()

    banner.banner()

    gameName = input(Fore.RED + "Inserisci il gioco da cercare: " + Fore.YELLOW)

    print(Fore.RESET)

    game = search.search(gameName)

    if game != 0:
        
        torrent = getTorrent.download(game)
    

        # Save the url


        text = (game.split("/")[-2].replace("-", " ")) + "  ->  " + torrent + "\n"

        cnt = 0


        if os.path.isfile("./torrents.txt"):
            f = open("./torrents.txt", "rt+")

            line = f.readline()

            while line != "":
            
                if text == line:
                    f.seek(cnt)
                    f.write(text)

                    break

                line = f.readline()
            else:
                f.write(text)

        else:
            f = open("./torrents.txt", "wt")

            f.write(text)

        f.close()

    print(Fore.RESET)