import os, requests, fade ;from colorama import Fore;from pystyle import * # Importamos las librerias que utilizaremos
w = Fore.LIGHTWHITE_EX;r = Fore.LIGHTRED_EX;g = Fore.LIGHTGREEN_EX;y = Fore.LIGHTYELLOW_EX;b = Fore.LIGHTBLUE_EX;m = Fore.LIGHTMAGENTA_EX;c = Fore.LIGHTCYAN_EX;black = Fore.LIGHTBLACK_EX # Definimos unas variables para los colores de la libreria Fore

# Las dos "GUI" que utilizaremos para estilizar el programa un poco
gui = """
    
            ╔═══════════════════════════════════════════════╗
            ║                                          . ╔══╣
            ║    ╦ ╦╔═╗╔╗ ╦ ╦╔═╗╔═╗╦╔═                 ╚═╝  ║
            ║    ║║║║╣ ╠╩╗╠═╣║ ║║ ║╠╩╗  franafp.com         ║
            ║    ╚╩╝╚═╝╚═╝╩ ╩╚═╝╚═╝╩ ╩   ╦  ╦  ╗            ║
            ║      ╔╗╔╦ ╦╦╔═╔═╗╦═╗       ╚╗╔╝  ║            ║
            ║      ║║║║ ║╠╩╗║╣ ╠╦╝        ╚╝   ╩            ║
            ║      ╝╚╝╚═╝╩ ╩╚═╝╩╚═    franafp.com           ║
            ╠══╗  .                .                  .     ║
            ╠╗   ╔╩═╗         ╔╩═╦═╩ ·               ╔╩═╗   ║
            ╚╩═══╩═══════════════╩══════════════════════╩═══╝
"""
gui_animated = """

╔═══════════════════════════════════════════════╗
║                                          . ╔══╣
║    ╦ ╦╔═╗╔╗ ╦ ╦╔═╗╔═╗╦╔═                 ╚═╝  ║
║    ║║║║╣ ╠╩╗╠═╣║ ║║ ║╠╩╗  wtp.franafp.com     ║
║    ╚╩╝╚═╝╚═╝╩ ╩╚═╝╚═╝╩ ╩   ╦  ╦  ╗            ║
║      ╔╗╔╦ ╦╦╔═╔═╗╦═╗       ╚╗╔╝  ║            ║
║      ║║║║ ║╠╩╗║╣ ╠╦╝        ╚╝   ╩            ║
║      ╝╚╝╚═╝╩ ╩╚═╝╩╚═    wtp.franafp.com       ║
╠══╗  .                .                  .     ║
╠╗   ╔╩═╗         ╔╩═╦═╩ ·               ╔╩═╗   ║
╚╩═══╩═══════════════╩══════════════════════╩═══╝
           Press enter for continue
"""
os.system("@mode con cols=150, lines=45 & cls & title Webhook Nuker v1.0 ^| wtp.franafp.com") # Definimos el tamaño de la terminal, limpiamos la terminal y asignamos un titulo a la terminal
Anime.Fade(Center.Center(gui_animated), Colors.rainbow, Colorate.Vertical, interval=0.1, enter=True) # Hacemos una animacion de la "GUI" que definimos anteriormente
faded_gui = fade.pinkred(gui) # Hacemos un fade a la "GUI" que definimos anteriormente

os.system("cls")
print(faded_gui) # Imprimimos la "GUI" que definimos anteriormente


def webhook_spammer(): 
    webhook = input(f"{m}[{w}>{m}] {black} Webhook -{m}> {y}") # Pedimos la webhook
    if r.status_code == 200: # Si la webhook es valida entonces pediremos el mensaje y el autor que quieren que aparezca
        print(f"{m}[{w}OK{m}] {g}Valid Webhook")
        message = input(f"{m}[{w}>{m}] {black} Message -{m}> {y}")
        author = input(f"{m}[{w}>{m}] {black} Author -{m}> {y}")
        while(True): # Ahora un búcle infinito que enviara el mensaje con el autor que definimos anteriormente
            requests.post(webhook, json={"content": message, "username": author})
            print(f"{m}[{w}SENT{m}] {g}Message sent")

webhook_spammer() # Llamamos a la función que definimos anteriormente