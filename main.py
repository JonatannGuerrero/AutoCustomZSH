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
    print("【3】 » Instalar plugins ZSH") # ZSH-syntax-highlighting, ZSH-Sudo, ZSH-autosuggestions
    print("【4】 » Instalar LSD, BAT y FZF")
    print("【5】 » Instalar Ranger")    
    print("【6】 » Instalar PowerLevel10k")
    print("【7】 » Instalar todo")
    print("【8】 » Salir")

    option = input("\n ➤ ") 
    if option=="1":
        os.system("clear")
        printBlue(banner)
        Option1()
        menu()            
    elif option=="2": 
        os.system("clear")
        printBlue(banner)
        Option2()  
        menu()      
    elif option=="3":
        os.system("clear")
        printBlue(banner)
        Option3()  
        menu()
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
    printWhite("【!】Obteniendo paquetes ...")
    time.sleep(1)
    printWhite("【!】Instalando requerimientos necesarios ...")
    time.sleep(1)
    #os.system("localectl set-x11-keymap es") 
    os.system("sudo apt-get update -y")    
    os.system("sudo apt install git python3-sphinx  -y")
    printGreen("【✔】 Requetimientos instalados correctamente") 
    time.sleep(1.5) 
    


# Opción 2 Instalando ZSH | Shell por defecto
def Option2():
    printWhite("【!】Obteniendo paquetes ...")
    os.system("sudo apt install zsh -y ") # Para Mac > "brew install zsh" 
    printGreen("【✔】 ZSH instalada")
    time.sleep(1.5) 
    os.system("sudo cp tools/zsh_conf ~/.zshrc")
    printYellow("【!】 Configurando ZSH 1/2 ...")
    time.sleep(1.5)
    user=os.environ['SUDO_USER']
    comand="sudo cp tools/zsh_conf /home/"+user+"/.zshrc"    
    os.system(comand)    
    comand="usermod --shell /usr/bin/zsh "+user    
    os.system(comand)    
    os.system("sudo chsh -s $(which zsh)")
    comand="ln -s -f /home/"+user+"/.zshrc ~/.zshrc"
    os.system(comand)  
    printYellow("【!】 Configurando ZSH 2/2 ... Done") 
    time.sleep(1.5)
    printGreen("【✔】 ZSH instalada y configurada correctamente")     
    time.sleep(1.5)    

# Instalando plugins ZSH
def Option3():
    printWhite("【!】Obteniendo paquetes ...")    
    os.system("sudo apt install zsh-syntax-highlighting zsh-autosuggestions -y")    
    os.mkdir('/usr/share/zsh-sudo')
    user=os.environ['SUDO_USER']
    comand="chown "+user+":"+user+" /usr/share/zsh-sudo"
    os.system(comand)
    comand="wget -P /usr/share/zsh-sudo/ https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/plugins/sudo/sudo.plugin.zsh"
    os.system(comand)    
    printGreen("【✔】 Plugins configurados e instados correctamente")
    time.sleep(1.5) 

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

