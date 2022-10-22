# -*- mode: python; coding: utf-8-with-signature-dos -*-

####################################################################################################
## Everything を起動するキーを指定する
####################################################################################################

try:
    # 設定されているか？
    fc.mintty_key
except:
    # Everything を起動するキーを指定する
    fc.mintty_key = "C-A-t"

try:
    # 設定されているか？
    fc.mintty_name
except:
    # Everything プログラムを指定する
    fc.mintty_name = r"C:\Users\ballo\AppData\Local\wsltty\bin\mintty.exe"

def mintty():
    keymap.ShellExecuteCommand(None, fc.mintty_name, r"--WSL= --configdir='C:\Users\ballo\AppData\Roaming\wsltty' -~  -", "")()

define_key(keymap_global, fc.mintty_key, mintty)
