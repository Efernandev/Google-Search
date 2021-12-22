import webbrowser 
from colorama import *
from os import *
import sys 
import time
init(autoreset=True)

def letter(message):
        for item in message:
            print(item,end="",flush=True)
            time.sleep(0.1)
        time.sleep(0.8)

def clean():
    if (sys.platform == 'win32'):
        system("cls")
    else:
        system("clear")

while True:
    print(f"{Fore.GREEN}({Fore.RED}?{Fore.GREEN}){Style.RESET_ALL} Nota{Fore.RED}:{Style.RESET_ALL} Script que faz você abrir uma url ou uma simples pesquisa para você na internet\nExemplo: {Fore.GREEN}'{Fore.YELLOW}url{Fore.GREEN} www.google.com'{Style.RESET_ALL} ou {Fore.GREEN}'Como se tornar um programador de sucesso!'{Style.RESET_ALL}\nComandos:\n- Escreva {Fore.RED}'clear'{Style.RESET_ALL} para dar clean no terminal\n- Escreva {Fore.RED}'exit'{Style.RESET_ALL} para fechar o script.")
    try:
        searchname = str(input(f"{Fore.LIGHTCYAN_EX}${Style.RESET_ALL} "))
        if (searchname == 'clear'):
            clean() # função que foi criado no intuito de fazer o terminal apagar todo o resto escrito em cima se adaptando a qualquer dispotisivo
        elif (searchname == 'exit'):
            print(f"\n[{Fore.RED}!{Style.RESET_ALL}] {Fore.CYAN}Usuário{Style.RESET_ALL} optou por finalizar o script{Fore.RED}.")
            sys.exit(0)
        else:
            if (searchname[0:3] == 'url'):
                webbrowser.open_new(searchname[4:])
                print("")
            else:
                webbrowser.open(f"https://www.google.com/search?q={searchname}")
                print("")
    except(KeyboardInterrupt):
        letter('\nSistema foi forçado a parar!')
        sys.exit(0)















