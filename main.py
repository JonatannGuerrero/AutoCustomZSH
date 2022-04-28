#!/usr/bin/python3

# Author: JonatannGuerrero | TheHackNotes.com

import os, time
from sys import stdout
import signal, sys, platform

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
def menu(Actu):  
    printBlue(banner)  
    print("【1】 » Instalar requerimientos necesarios")
    print("【2】 » Instalar y configurar ZSH")    
    print("【3】 » Instalar plugins ZSH") # ZSH-syntax-highlighting, ZSH-Sudo, ZSH-autosuggestions
    print("【4】 » Instalar PowerLevel10k")
    print("【5】 » Instalar utilidades")  
    print("【6】 » Instalar todo")
    print("【7】 » Salir")

    option = input("\n ➤ ") 
    if option=="1":
        os.system("clear")
        printBlue(banner)
        Option1(Actu)
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
        os.system("clear")
        printBlue(banner)
        Option4()  
        menu()        
    elif option=="5":
        os.system("clear")
        printBlue(banner)
        Option5()  
        menu()         
    elif option=="6":
        os.system("clear")
        printBlue(banner)
        Option1(Actu)
        Option2()
        Option3()
        Option4()
        Option5()
        printGreen("【★】AutoCustomZSH Done | TheHackNotes.com")  
        time.sleep(1.5)  
        printYellow("【★】Saliendo ...") 
        time.sleep(1) 
    elif option=="7":
        printYellow("\n【★】Saliendo ...")        
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
def Option1(Actu):    
    printWhite("【!】Obteniendo paquetes ...")
    time.sleep(1)        
    os.system("sudo apt-get update -y")
    if Actu:
        printWhite("【!】Actualizando sistema ...")
        time.sleep(1) 
        os.system("sudo apt upgrade -y")  
    else:
        printYellow("【!】Si presenta errores en la instalación, actualice el sistema.")
        time.sleep(1)
    printWhite("【!】Instalando requerimientos necesarios ...")
    time.sleep(1) 
    os.system("sudo apt install git scrub python3-sphinx -y")
    printGreen("【✔】 Requerimientos instalados correctamente") 
    time.sleep(1.5) 

# Opción 2 Instalando ZSH | Shell por defecto | !rmk Lista
def Option2():
    printWhite("【!】Obteniendo paquetes ZSH...")
    os.system("sudo apt install zsh -y ") # Para Mac > "brew install zsh" 
    printGreen("【✔】 ZSH instalada")
    time.sleep(1.5) 
    os.system("sudo cp tools/zsh_conf ~/.zshrc")
    printYellow("【!】 Configurando ZSH 1/2 ...")
    time.sleep(1.5)    
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
    printWhite("【!】Obteniendo plugins ZSH ...")    
    os.system("sudo apt install zsh-syntax-highlighting zsh-autosuggestions -y")    
    os.mkdir('/usr/share/zsh-sudo')    
    comand="chown "+user+":"+user+" /usr/share/zsh-sudo"
    os.system(comand)
    comand="wget -P /usr/share/zsh-sudo/ https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/plugins/sudo/sudo.plugin.zsh"
    os.system(comand)    
    printGreen("【✔】 Plugins configurados e instados correctamente")
    time.sleep(1.5) 


# Instalando PowerLevel10k
def Option4():
    printWhite("【!】Obteniendo paquetes PowerLevel10k ...") 
    os.system("git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/powerlevel10k")
    comand="sudo git clone --depth=1 https://github.com/romkatv/powerlevel10k.git /home/"+user+"/powerlevel10k"
    os.system(comand) 
    os.system("sudo cp tools/p10k_conf ~/.p10k.zsh")
    comand="sudo cp tools/p10k_conf /home/"+user+"/.p10k.zsh" 
    os.system(comand)  
    printGreen("【✔】PowerLevel10k instalada correctamente")
    time.sleep(1.5)   

# Instalando LSD, BAT, FZF, Ranger
def Option5():
    printWhite("【!】Obteniendo utilidades ...") 
    os.system("sudo apt install bat -y")
    os.system("sudo dpkg -i tools/lsd_0.21.0_amd64.deb")
    comand="git clone --depth 1 https://github.com/junegunn/fzf.git /home/"+user+"/.fzf" # ctrl+r ó ctrl+t
    os.system(comand)
    comand="/home/"+user+"/.fzf/install --all"
    os.system(comand)    
    comand="chown -R "+user+":"+user+" /home/"+user+"/.fzf"
    os.system(comand)    
    comand="cp ~/.fzf.zsh /home/"+user+"/.fzf.zsh"
    os.system(comand)        
    os.system("sudo apt install ranger -y")
    printGreen("【✔】Utilidades Listas")
    time.sleep(1.5)


def Linux():
    printBlue(banner)
    print("【1】 » Actualizar paquetes del sistema (RECOMENDADO)")
    print("【2】 » Continuar sin actualizar")
    option = input("\n ➤ ") 
    if option=="1":
        menu(True)
    elif option=="2":
        menu(False)
    else:
        printRed("\n【✘】Opción invalida")
        printYellow("【!】Se continuará sin actualizar")
        time.sleep(1)
        menu(False)

def MacOS():
    printYellow("\n【!】Herramienta para MacOS en construcción ...")
    time.sleep(0.5)
    printYellow("【★】Saliendo ... \n")
    time.sleep(1)

if __name__ == '__main__': 
    signal.signal(signal.SIGINT, signal_handler)     
    id = os.getuid()   
    if id == 0:
        user=os.environ['SUDO_USER']        
        if platform.system()=='Darwin':
            MacOS()
        elif platform.system()=="Linux":            
            Linux()
        else:
            printBlue(banner)
            printRed("\n【✘】No se reconoce el sistema operativo \n") 
            time.sleep(0.8)
            print("【1】 » Ubuntu, Parrot, Kali, WSL")
            print("【2】 » MacOS")
            option = input("\n ➤ ") 
            if option=="1":                
                Linux()
            elif option=="2":
                MacOS()
            else:
                printRed("\n【✘】Opción invalida")
                time.sleep(0.8)
                printYellow("【!】Intente nuevamente")
                printYellow("【★】Saliendo ... \n")
                time.sleep(0.5)
    else:        
        printBlue(banner)
        printYellow("\n【!】La herramienta requiere ejecutarse como root")
        time.sleep(0.5)         
        printRed("\n【✘】Intente nuevamente como root \n")
        time.sleep(1.3)

