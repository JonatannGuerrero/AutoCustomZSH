#!/usr/bin/python3

# Author: JonatannGuerrero | TheHackNotes.com

import os, time
from sys import stdout

# Colores

def printRed(text):
    WHITE= "\033[1;37m"
    RED = "\033[1;31m" 
    stdout.write(RED)
    print(text)
    stdout.write(WHITE)

def printGreen(text):
    WHITE= "\033[1;37m"
    GREEN = "\033[0;32m"
    stdout.write(GREEN)
    print(text)
    stdout.write(WHITE)

def printBlue(text):
    WHITE= "\033[1;37m"
    BLUE = "\033[1;34m"
    stdout.write(BLUE)
    print(text)
    stdout.write(WHITE)

def printYellow(text):
    WHITE= "\033[1;37m"
    YELLOW = "\033[1;33m"
    stdout.write(YELLOW)
    print(text)
    stdout.write(WHITE)

banner = """

                      █████╗ ██╗   ██╗████████╗ ██████╗                        
                     ██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗                       
                     ███████║██║   ██║   ██║   ██║   ██║                       
                     ██╔══██║██║   ██║   ██║   ██║   ██║                       
                     ██║  ██║╚██████╔╝   ██║   ╚██████╔╝                       
                     ╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝                        

  ██████╗██╗   ██╗███████╗████████╗ ██████╗ ███╗   ███╗███████╗███████╗██╗  ██╗
 ██╔════╝██║   ██║██╔════╝╚══██╔══╝██╔═══██╗████╗ ████║╚══███╔╝██╔════╝██║  ██║
 ██║     ██║   ██║███████╗   ██║   ██║   ██║██╔████╔██║  ███╔╝ ███████╗███████║
 ██║     ██║   ██║╚════██║   ██║   ██║   ██║██║╚██╔╝██║ ███╔╝  ╚════██║██╔══██║
 ╚██████╗╚██████╔╝███████║   ██║   ╚██████╔╝██║ ╚═╝ ██║███████╗███████║██║  ██║
  ╚═════╝ ╚═════╝ ╚══════╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝©
                                TheHackNotes.com
"""


# Menu de opciones 
def menu():  
    printBlue(banner)  
    print("【1】 » Instalar requerimientos necesarios")
    print("【2】 » Instalar ZSH")
    print("【3】 » Instalar plugins ZSH") # ZSH-syntax-highlighting, ZSH-Sudo, ZSH-autosuggestions
    print("【4】 » Instalar LSD, BAT y FZF")
    print("【5】 » Instalar Ranger")
    print("【6】 » Configurar ZSH por defecto")
    print("【7】 » Instalar PowerLevel10k")
    print("【8】 » Instalar todo")
    print("【9】 » Salir")

    option = input("\n ➤ ") 
    if option=="1":
        printGreen("\n【★】Instalando requerimientos necesarios ...")
    elif option=="2": 
        printGreen("\n【★】Instalando ZSH ...")
    elif option=="3":
        printGreen("\n【★】Instalando plugins ZSH ...")
    elif option=="4":
        printGreen("\n【★】Instalando LSD, BAT y FZF ...")
    elif option=="5":
        printGreen("\n【★】Instalando Ranger ...")
    elif option=="6":
        printGreen("\n【★】Configurar ZSH por defecto ....")
    elif option=="7":
        printGreen("\n【★】Instalando PowerLevel10k ....")
    elif option=="8":
        printGreen("\n【★】Personalizando todo ....")
    elif option=="9":
        printYellow("\n【★】Saliendo ...")
    else:
        os.system("clear")
        printBlue(banner)
        printRed("\n【★】Opción invalida")
        time.sleep(0.5)
        printRed("\n【★】Intente nuevamente")        
        time.sleep(1.3)
        os.system("clear")
        menu()        


# Opción 1 Requerimientos
def Option1():
    print("【★】")




if __name__ == '__main__':
    id = os.getuid()    
    if id == 0:        
        print("[!] No hay que ser root para ejecutar la herramienta")
        
    else:        
        menu()
        






# PASOS

# 1 Actualizar los paquetes del sistemas python3 git
# 2 instalar zsh (" sudo apt install zsh -y ")


# Instalamos lsd y bat 