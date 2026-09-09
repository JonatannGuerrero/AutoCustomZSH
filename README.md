# AutoCustomZSH 👨‍💻 
AutoCustomZSH es un script que automatiza e integra diferentes herramientas disponibles en Github, las cuales hacen posible que la terminal se vea estética, además de aplicar cambios que la hacen más interactiva y funcional. 
*[Más información sobre AutoCustomZSH](https://blog.thehacknotes.com/p/personalizaci%C3%B3n-de-la-terminal/)*
## Instalación

Para hacer uso del script se debe ejecutar como root, ya que este realiza cambios en el sistema:  ↴

```bash 
git clone https://github.com/JonatannGuerrero/AutoCustomZSH.git
cd AutoCustomZSH/
sudo python3 install.py
```
> 👉 El script fue probado en Kali, Parrot y Ubuntu. Funciona bien para sistemas operativos basados en Debian.

### 🍎 macOS

En macOS el script instala todo mediante **Homebrew**, que es un prerrequisito. Si aún no lo tiene, instálelo **sin sudo**:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Después ejecute el script con `sudo` igual que en Linux. Homebrew no puede correr como root, así que el script baja los privilegios al usuario que invocó `sudo` para cada instalación.

> 👉 macOS ya trae **zsh** como shell por defecto, por lo que ese paso se omite. El archivo de configuración usado es `tools/zsh_conf_macos`.

> 👉 Para que se vean los iconos de Powerlevel10k debe seleccionar **MesloLGS Nerd Font** en las preferencias de su terminal (Terminal.app o iTerm2). El script instala la fuente, pero no puede seleccionarla por usted.

# 📟 Utilidades

- **ZSH** : Shell. 
- **Powerlevel10k** : Tema Shell.
- **LSD** : Alternativa a ls (*Alias definido en `~/.zshrc`*).
- **Bat** : Alternativa a cat (*Alias definido en `~/.zshrc`*).
- **Plugins ZSH** : zsh-syntax-highlighting, zsh-Sudo, zsh-autosuggestions.
- **Ranger** : Administrador de archivos para la terminal.
- **FZF** : Buscador en línea de comandos.

# 💥🚨💥 Importante 

- El script configura ***zsh*** como shell por defecto.
- Archivo de configuración `~/.zshrc`.
- Ejecute `p10k configure` para cambiar el tema de la terminal.
- <kbd>Ctrl</kbd> + <kbd>R</kbd> : Historial de comandos.  
- <kbd>Ctrl</kbd>+ <kbd>T</kbd> : Busca archivos en el directorio actual.
- <kbd>ESC</kbd> : Se presiona dos veces y agrega ***sudo*** al comando.
- Ejecute `ranger` para abrir un administrador de archivos para la terminal; **q** para salir. 

# 🧾 Referencias

- *[[1] 	Github: @Peltoche, «LSD (LSDeluxe)», 16 Enero 2022. [En línea].](https://github.com/Peltoche/lsd)*

- *[[2] 	Github: @junegunn, «fzf Command-line fuzzy finder», 4 abril 2022. [En línea].](https://github.com/junegunn/fzf)*

- *[[3] 	Github: @romkatv, «Powerlevel10k», 2 febrero 2022. [En línea].](https://github.com/romkatv/powerlevel10k)*

- *[[4] 	Github: @sharkdp, «A cat clone with syntax highlighting and Git integration.», 27 febrero 2022. [En línea].](https://github.com/sharkdp/bat)*
# 🔧 Built With
- Python3
# 📝 License
GNU General Public License © 2022 | JonatannGuerrero