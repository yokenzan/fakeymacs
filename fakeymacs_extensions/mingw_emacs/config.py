# -*- mode: python; coding: utf-8-with-signature-dos -*-

####################################################################################################
## Everything を起動するキーを指定する
####################################################################################################

try:
    # 設定されているか？
    fc.mingw_emacs_key
except:
    # Emacs を起動するキーを指定する
    fc.mingw_emacs_key = "C-A-e"

try:
    # 設定されているか？
    fc.mingw_emacs_name
except:
    # Everything プログラムを指定する
    fc.mingw_emacs_name = r"C:\Users\ballo\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\start_mingw64_emacs28.cmd"

def mingw_emacs():
    keymap.ShellExecuteCommand(None, fc.mingw_emacs_name, r"--WSL= --configdir='C:\Users\ballo\AppData\Roaming\wsltty' -~  -", "")()

define_key(keymap_global, fc.mingw_emacs_key, mingw_emacs)
