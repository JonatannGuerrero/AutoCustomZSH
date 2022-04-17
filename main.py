#!/usr/bin/python3

# Author: JonatannGuerrero | TheHackNotes.com

import os, time
from sys import stdout
import signal
import sys

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

def printWhite(text):
    WHITE= "\033[1;37m"    
    stdout.write(WHITE)
    print(text)

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
# Detener procesos
def signal_handler(sig, frame):
    printBlue(banner) 
    printRed("\n【✘】Procesos cancelados")
    time.sleep(1)
    printYellow("\n【★】Saliendo ...\n")    
    sys.exit(0)

# Menu de opciones 
def menu():  
    printBlue(banner)  
    print("【1】 » Instalar requerimientos necesarios")
    print("【2】 » Instalar y configurar ZSH")    
    print("【4】 » Instalar plugins ZSH") # ZSH-syntax-highlighting, ZSH-Sudo, ZSH-autosuggestions
    print("【5】 » Instalar LSD, BAT y FZF")
    print("【6】 » Instalar Ranger")    
    print("【7】 » Instalar PowerLevel10k")
    print("【8】 » Instalar todo")
    print("【9】 » Salir")

    option = input("\n ➤ ") 
    if option=="1":
        Option1()             
    elif option=="2": 
        Option2()        
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
        printYellow("\n【★】Saliendo ...\n")
    else:
        os.system("clear")
        printBlue(banner)
        printRed("\n【✘】Opción invalida")
        time.sleep(0.8)
        printYellow("\n【!】Intente nuevamente")        
        time.sleep(1.5)
        os.system("clear")
        menu()        


# Opción 1 Requerimientos
def Option1():
    os.system("clear")
    printBlue(banner)
    printGreen("\n【!】Instalando requerimientos necesarios ...")
    time.sleep(1)
    printWhite("【!】Obteniendo paquetes ...")
    os.system("sudo apt-get update -y")    
    os.system("sudo apt install git python3-sphinx  -y")
    printGreen("\n【✔】 Requetimientos instalados correctamente") 
    time.sleep(1.5)    
    menu()

# Opción 2 Instalando ZSH | Shell por defecto
def Option2():
    os.system("clear")
    printBlue(banner)    
    printWhite("【!】Obteniendo paquetes ...")
    os.system("sudo apt install zsh -y ") # Para Mac > "brew install zsh"
    os.system("sudo chsh -s $(which zsh)") # Cambia la Shell
    os.system("cp tools/zsh_conf ~/.zshrc")
    printGreen("\n【✔】 ZSH instalada y configurada correctamente")     
    time.sleep(1.5)    
    menu()


if __name__ == '__main__': 
    signal.signal(signal.SIGINT, signal_handler)     
    id = os.getuid()   
    if id == 0:
        menu()
    else:
        printBlue(banner)
        printYellow("\n【!】La herramineta requiere ejecutarse como root")
        time.sleep(0.5)         
        printRed("\n【✘】Intente nuevamente como root")
        time.sleep(1.3)

