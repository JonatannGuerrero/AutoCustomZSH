# AutoCustomZSH 👨‍💻 
AutoCustomZSH es un script que automatiza e integra diferentes herramientas disponibles en Github, las cuales hacen posible que la terminal se vea estética, además de aplicar cambios que la hacen más interactiva y funcional. 
*[Más información sobre AutoCustomZSH](https://blog.thehacknotes.com/p/personalizaci%C3%B3n-de-la-terminal/)*
## Instalación

```bash 
git clone https://github.com/JonatannGuerrero/AutoCustomZSH.git
cd AutoCustomZSH/
python3 install.py
```
> 👉 El script fue probado en Kali, Parrot y Ubuntu. Funciona bien para sistemas operativos basados en Debian. *Integración para MacOS en proceso* ... 👨‍💻

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

- *[[1] 	Sergiu Gatlan, «Windows Terminal now can automatically launch profiles as Administrator», 3 Febrero 2022. [Imagen Post]. [En línea].](https://www.bleepingcomputer.com/news/microsoft/windows-terminal-now-can-automatically-launch-profiles-as-administrator/)*

- *[[2] 	Github: @Peltoche, «LSD (LSDeluxe)», 16 Enero 2022. [En línea].](https://github.com/Peltoche/lsd)*

- *[[3] 	Github: @junegunn, «fzf Command-line fuzzy finder», 4 abril 2022. [En línea].](https://github.com/junegunn/fzf)*

- *[[4] 	Github: @romkatv, «Powerlevel10k», 2 febrero 2022. [En línea].](https://github.com/romkatv/powerlevel10k)*

- *[[5] 	Github: @sharkdp, «A cat clone with syntax highlighting and Git integration.», 27 febrero 2022. [En línea].](https://github.com/sharkdp/bat)*
# 🔧 Built With
- Python3
# 📝 License
GNU General Public License © 2022 | JonatannGuerrero