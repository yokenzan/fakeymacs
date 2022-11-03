﻿# -*- mode: python; coding: utf-8-with-signature-dos -*-

# https://stackoverflow.com/questions/2904274/globals-and-locals-in-python-exec
# https://docs.python.org/3/library/functions.html?highlight=exec%20global#exec

# 本ファイルは、config_personal.py というファイル名にすることで個人設定ファイルとして機能します。
# 本ファイルの設定には [] で括られたセクション名が定義されており、その単位で config.py の中に設定
# が取り込まれ、exec関数により実行されます。config.py ファイル内の exec関数をコールしているところ
# を検索すると、何のセクションがどこで読み込まれるかが分かると思います。

# 本ファイルはサンプルファイルです。本ファイルに記載のない設定でも、config.py から設定を取り込み、
# カスタマイズしてご利用ください。

####################################################################################################
## 初期設定
####################################################################################################
# [section-init] -----------------------------------------------------------------------------------

print(startupString())

# def editor(path):
#     shellExecute( None, None, r"wslg.exe ~ -d Ubuntu-20.04 emacs27 ", '"%s"'% path, "" )

keymap.editor = r"C:\Users\ballo\tools\sakura\sakura.exe"
# keymap.editor = editor
# keymap.editor = r"wslg.exe ~ -d Ubuntu-20.04 emacs27 "
keymap.setFont("Sarasa Term Slab TC", 16)

####################################################################################################
## 機能オプションの選択
####################################################################################################
# [section-options] --------------------------------------------------------------------------------

# IMEの設定（次の設定のいずれかを有効にする）
# fc.ime = "old_Microsoft_IME"
# fc.ime = "new_Microsoft_IME"
# fc.ime = "Google_IME"
fc.ime = None

####################################################################################################
## 基本設定
####################################################################################################
# [section-base-1] ---------------------------------------------------------------------------------

# Emacs のキーバインドに“したくない”アプリケーションソフトを指定する
# （Keyhac のメニューから「内部ログ」を ON にすると processname や classname を確認することができます）
fc.not_emacs_target     = ["wsl.exe",                # WSL
                           "wslg.exe",
                           "skks.exe",
                           "skkx.exe",
                           "skk.exe",
                           "idea64.exe",
                           "bash.exe",               # WSL
                           "ubuntu.exe",             # WSL
                           "ubuntu1604.exe",         # WSL
                           "ubuntu1804.exe",         # WSL
                           "ubuntu2004.exe",         # WSL
                           "debian.exe",             # WSL
                           "kali.exe",               # WSL
                           "SLES-12.exe",            # WSL
                           "openSUSE-42.exe",        # WSL
                           "openSUSE-Leap-15-1.exe", # WSL
                           "mstsc.exe",              # Remote Desktop
                           "WindowsTerminal.exe",    # Windows Terminal
                           "mintty.exe",             # mintty
                           "wsltty.exe",             # mintty
                           "Cmder.exe",              # Cmder
                           "ConEmu.exe",             # ConEmu
                           "ConEmu64.exe",           # ConEmu
                           "emacs.exe",              # Emacs
                           "emacs-X11.exe",          # Emacs
                           "emacs-w32.exe",          # Emacs
                           "gvim.exe",               # GVim
                           "xyzzy.exe",              # xyzzy
                           "VirtualBox.exe",         # VirtualBox
                           "msrdc.exe",              # WSLg
                           "XWin.exe",               # Cygwin/X
                           "XWin_MobaX.exe",         # MobaXterm/X
                           "XWin_MobaX_1.16.3.exe",  # MobaXterm/X
                           "XWin_Cygwin_1.14.5.exe", # MobaXterm/X
                           "XWin_Cygwin_1.16.3.exe", # MobaXterm/X
                           "Xming.exe",              # Xming
                           "vcxsrv.exe",             # VcXsrv
                           "GWSL_vcxsrv.exe",        # GWSL
                           "GWSL_vcxsrv_lowdpi.exe", # GWSL
                           "X410.exe",               # X410
                           "Xpra-Launcher.exe",      # Xpra
                           "putty.exe",              # PuTTY
                           "ttermpro.exe",           # TeraTerm
                           "MobaXterm.exe",          # MobaXterm
                           "TurboVNC.exe",           # TurboVNC
                           "vncviewer.exe",          # UltraVNC
                           "vncviewer64.exe",        # UltraVNC
                           ]

# IME の切り替え“のみをしたい”アプリケーションソフトを指定する
# （指定できるアプリケーションソフトは、not_emacs_target で（除外）指定したものからのみとなります）
fc.ime_target          += []

# キーマップ毎にキー設定をスキップするキーを指定する
# （リストに指定するキーは、define_key の第二引数に指定する記法のキーとしてください。"A-v" や "C-v"
#   のような指定の他に、"M-f" や "Ctl-x d" などの指定も可能です。"M-g*" のようにワイルドカードも
#   利用することができます。）
# （ここで指定したキーに新たに別のキー設定をしたいときには、「-2」が付くセクション内で define_key2
#   関数を利用して定義してください）
fc.skip_settings_key    = {"keymap_global"    : [], # 全画面共通 Keymap
                           "keymap_emacs"     : [], # Emacs キーバインド対象アプリ用 Keymap
                           "keymap_ime"       : [], # IME 切り替え専用アプリ用 Keymap
                           "keymap_ei"        : [], # Emacs 日本語入力モード用 Keymap
                           "keymap_tsw"       : [], # タスク切り替え画面用 Keymap
                           "keymap_lw"        : [], # リストウィンドウ用 Keymap
                           }

# Emacs のキーバインドにするアプリケーションソフトで、Emacs キーバインドから除外するキーを指定する
# （リストに指定するキーは、Keyhac で指定可能なマルチストロークではないキーとしてください。
#   Fakeymacs の記法の "M-f" や "Ctl-x d" などの指定はできません。"A-v"、"C-v" などが指定可能です。）
fc.emacs_exclusion_key  = {"chrome.exe"       : ["C-l", "C-t"],
                           "msedge.exe"       : ["C-l", "C-t"],
                           "firefox.exe"      : ["C-l", "C-t"],
                           "Code.exe"         : ["C-S-b", "C-S-f", "C-S-p", "C-S-n", "C-S-a", "C-S-e"],
                           }

# 左右どちらの Ctrlキーを使うかを指定する（"L": 左、"R": 右）
fc.side_of_ctrl_key = "L"

# Escキーを Metaキーとして使うかどうかを指定する（True: 使う、False: 使わない）
# （True（Metaキーとして使う）に設定されている場合、ESC の二回押下で ESC が入力されます）
fc.use_esc_as_meta = False

# Emacs日本語入力モードを使うかどうかを指定する（True: 使う、False: 使わない）
fc.use_emacs_ime_mode = False

# Emacs日本語入力モードが有効なときに表示するバルーンメッセージを指定する
# fc.emacs_ime_mode_balloon_message = None
fc.emacs_ime_mode_balloon_message = "▲"

# IME の状態を表示するバルーンメッセージを表示するかどうかを指定する（True: 表示する、False: 表示しない）
fc.use_ime_status_balloon = True

# IME をトグルで切り替えるキーを指定する（複数指定可）
fc.toggle_input_method_key = []
fc.toggle_input_method_key += []
# fc.toggle_input_method_key += ["C-Yen"]
# fc.toggle_input_method_key += ["C-o"]
# fc.toggle_input_method_key += ["O-LAlt"]

#---------------------------------------------------------------------------------------------------
# IME を切り替えるキーの組み合わせ（disable、enable の順）を指定する（複数指定可）
# （toggle_input_method_key のキー設定より優先します）
fc.set_input_method_key = []

## 日本語キーボードを利用している場合、<無変換> キーで英数入力、<変換> キーで日本語入力となる
# fc.set_input_method_key += [["(29)", "(28)"]]

## 日本語キーボードを利用している場合、<Ａ> キーで英数入力、<あ> キーで日本語入力となる
## （https://docs.microsoft.com/ja-jp/windows-hardware/design/component-guidelines/keyboard-japan-ime）
# fc.set_input_method_key += [["(26)", "(22)"]]

## LAlt の単押しで英数入力、RAlt の単押しで日本語入力となる
## （JetBrains 製の IDE でこの設定を利用するためには、ツールボタンをオンにする必要があるようです。
##   設定は、View -> Appearance -> Tool Window Bars を有効にしてください。）
# fc.set_input_method_key += [["O-LAlt", "O-RAlt"]]

## C-j や C-j C-j で 英数入力となる（toggle_input_method_key の設定と併せ、C-j C-o で日本語入力となる）
# fc.set_input_method_key += [["C-j", None]]

## C-j で英数入力、C-o で日本語入力となる（toggle_input_method_key の設定より優先）
# fc.set_input_method_key += [["C-j", "C-o"]]

## C-j で英数入力、C-i で日本語入力となる（C-i が Tab として利用できなくなるが、トグルキー C-o との併用可）
# fc.set_input_method_key += [["C-j", "C-i"]]
#---------------------------------------------------------------------------------------------------

# アプリケーションキーとして利用するキーを指定する
# （修飾キーに Alt は使えないようです）
# fc.application_key = "O-RCtrl"
# fc.application_key = "W-m"

# 数引数の指定に Ctrl+数字キーを使うかを指定する（True: 使う、False: 使わない）
# （False に指定しても、C-u 数字キーで数引数を指定することができます）
# fc.use_ctrl_digit_key_for_digit_argument = True

# ウィンドウのリストアが最小化した順番の逆順とならない場合の対策を行うかを指定する
# （True: 対策有、False: 対策無）
fc.reverse_window_to_restore = False

# [section-base-2] ---------------------------------------------------------------------------------

####################################################################################################
## クリップボードリストの設定
####################################################################################################
# [section-clipboardList-1] ------------------------------------------------------------------------

# 定型文
fc.age_items = [
    ["生年月日未就学児",    datetime.date(datetime.date.today().year -  3, 7, 28).strftime("%Y.%m.%d")],
    ["生年月日一般",        datetime.date(datetime.date.today().year - 50, 7, 28).strftime("%Y.%m.%d")],
    ["生年月日高齢受給者",  datetime.date(datetime.date.today().year - 72, 7, 28).strftime("%Y.%m.%d")],
    ["生年月日後期高齢者",  datetime.date(datetime.date.today().year - 80, 7, 28).strftime("%Y.%m.%d")],
]
# fc.insurer_number_items = [
#     ["69国保",       "010108"],
#     ["39後期高齢",   "39016019"],
#     ["01協会けんぽ", "01010016"],
#     ["54指定難病",   "54016019"],
#     # ["---------+ x 8", "---------+" * 8],
#     # ["メールアドレス", "user_name@domain_name"],
#     # ["住所",           "〒999-9999 ＮＮＮＮＮＮＮＮＮＮ"],
#     # ["電話番号",       "99-999-9999"],
# ]
# fc.fixed_items[0][0] = list_formatter.format(fc.fixed_items[0][0])

# 日時
fc.datetime_items = [
    ["YYYY.MM.DD",          dateAndTime("%Y.%m.%d")],
    ["YYYY-MM-DD",          dateAndTime("%Y-%m-%d")],
    ["2022-04-01",          datetime.datetime(2022, 4, 1).strftime("%Y.%m.%d")],
    ["2022.04.01",          datetime.datetime(2022, 4, 1).strftime("%Y-%m-%d")],
    ["HH:MM:SS",            dateAndTime("%H:%M:%S")],
    ["YYYYMMDD_HHMMSS",     dateAndTime("%Y%m%d_%H%M%S")],
    ["YYYYMMDD",            dateAndTime("%Y%m%d")],
    ["HHMMSS",              dateAndTime("%H%M%S")],
]
fc.datetime_items[0][0] = list_formatter.format(fc.datetime_items[0][0])

fc.clipboardList_listers = [
    ["現在日時",               cblister_FixedPhrase(fc.datetime_items)],
    ["生年月日",               cblister_FixedPhrase(fc.age_items)],
    # ["保険者・公費負担者番号", cblister_FixedPhrase(fc.insurer_number_items)],
]

# [section-clipboardList-2] ------------------------------------------------------------------------

####################################################################################################
## ランチャーリストの設定
####################################################################################################
# [section-lancherList-1] --------------------------------------------------------------------------

# アプリケーションソフト



# ウェブサイト
fc.website_items = [
    ["Google",          keymap.ShellExecuteCommand(None, r"https://www.google.co.jp/", "", "")],
    # ["Facebook",        keymap.ShellExecuteCommand(None, r"https://www.facebook.com/", "", "")],
    # ["twitter",         keymap.shellexecutecommand(none, r"https://twitter.com/", "", "")],
    ["Keyhac",          keymap.ShellExecuteCommand(None, r"https://sites.google.com/site/craftware/keyhac-ja", "", "")],
    ["Fakeymacs",       keymap.ShellExecuteCommand(None, r"https://github.com/smzht/fakeymacs", "", "")],
    # ["NTEmacs＠ウィキ", keymap.ShellExecuteCommand(None, r"https://w.atwiki.jp/ntemacs/", "", "")],
]
fc.website_items[0][0] = list_formatter.format(fc.website_items[0][0])

# その他
fc.other_items = [
    ["Edit   config.py", keymap.command_EditConfig],
    ["Reload config.py", keymap.command_ReloadConfig],
]
fc.other_items[0][0] = list_formatter.format(fc.other_items[0][0])

fc.lancherList_listers = [
    # ["Website", cblister_FixedPhrase(fc.website_items)],
    # ["Other",   cblister_FixedPhrase(fc.other_items)],
]

# [section-lancherList-2] --------------------------------------------------------------------------

####################################################################################################
## 拡張機能の設定
####################################################################################################
# [section-extensions] -----------------------------------------------------------------------------

# https://github.com/smzht/fakeymacs/blob/master/fakeymacs_manuals/extensions.org

# --------------------------------------------------------------------------------------------------

# VSCode 用のキーの設定を行う
if 0:
    fc.vscode_target  = ["Code.exe"]
    # vscode.dev 等、ブラウザで動作する VSCode で本機能を無効とするには、次の４行をコメントアウト
    # してください
    fc.vscode_target += ["chrome.exe",
                         "msedge.exe",
                         "firefox.exe",
                         ]
    # fc.vscode_prefix_key = [["C-;", "C-A-;"]]
    fc.use_ctrl_atmark_for_mark = False
    fc.use_direct_input_in_vscode_terminal = False
    fc.esc_mode_in_keyboard_quit = 1

    # VSCode Extension 用のキーの設定を行う
    fc.vscode_dired = False
    fc.vscode_recenter = False
    fc.vscode_occur = False
    fc.vscode_quick_select = True
    fc.vscode_input_sequence = True
    fc.vscode_insert_numbers = True
    fc.vscode_keyboard_macro = False

    exec(readConfigExtension(r"vscode_key\config.py"), dict(globals(), **locals()))
    # vscode_extensions\config.py は、vscode_key\config.py 内部から呼ばれている

# --------------------------------------------------------------------------------------------------

# Everything を起動するキーを指定する
if 1:
    exec(readConfigExtension(r"everything\config.py"), dict(globals(), **locals()))

# --------------------------------------------------------------------------------------------------

# ブラウザをポップアップしてから C-l、C-t を入力するキーを設定する
if 0:
    exec(readConfigExtension(r"browser_key\config.py"), dict(globals(), **locals()))

# --------------------------------------------------------------------------------------------------

# Chrome 系ブラウザで Ctl-x C-b を入力した際、Chrome の拡張機能 Quick Tabs を起動する
# （vscode_key Extension で vscode_target に Chrome 系ブラウザを指定している場合、そちらの
#   キー設定が優先されます）
if 1:
    fc.chrome_list= ["vivaldi.exe"]
    fc.quick_tabs_shortcut_key = "F2"
    exec(readConfigExtension(r"chrome_quick_tabs\config.py"), dict(globals(), **locals()))

# --------------------------------------------------------------------------------------------------

# Emacs の shell-command-on-region の機能をサポートする
if 0:
    fc.unix_tool = "WSL"
    # fc.unix_tool = "MSYS2"
    # fc.unix_tool = "Cygwin"
    # fc.unix_tool = "BusyBox"
    # fc.bash_options = []
    fc.bash_options = ["-l"]
    exec(readConfigExtension(r"shell_command_on_region\config.py"), dict(globals(), **locals()))

# --------------------------------------------------------------------------------------------------

# 指定したアプリケーションソフトに F2（編集モード移行）を割り当てるキーを設定する
if 0:
    exec(readConfigExtension(r"edit_mode\config.py"), dict(globals(), **locals()))

# --------------------------------------------------------------------------------------------------

# Emacs の場合、IME 切り替え用のキーを C-\ に置き換える
if 0:
    exec(readConfigExtension(r"real_emacs\config.py"), dict(globals(), **locals()))

# --------------------------------------------------------------------------------------------------

# 英語キーボード設定をした OS 上で日本語キーボードを利用する場合の設定を行う
if 0:
    fc.change_keyboard_startup = "US"
    # fc.change_keyboard_startup = "JP"
    exec(readConfigExtension(r"change_keyboard\config.py"), dict(globals(), **locals()))

# --------------------------------------------------------------------------------------------------

# クリップボードに格納したファイルもしくはフォルダのパスを emacsclient で開く
if 0:
    fc.emacsclient_name = r"<emacsclient プログラムをインストールしている Windows のパス>\wslclient-n.exe"
    exec(readConfigExtension(r"emacsclient\config.py"), dict(globals(), **locals()))

# --------------------------------------------------------------------------------------------------

# 指定したキーを押下したときに IME の状態を表示する
if 0:
    fc.pop_ime_balloon_key = ["C-Semicolon"]
    # fc.pop_ime_balloon_key = ["O-" + fc.side_of_ctrl_key + "Ctrl"] # Ctrl キーの単押し
    exec(readConfigExtension(r"pop_ime_balloon\config.py"), dict(globals(), **locals()))

# --------------------------------------------------------------------------------------------------

# 60% US キーボードのキー不足（Delete キー、Backquote キー不足）の対策を行う
if 0:
    exec(readConfigExtension(r"compact_keyboard\config.py"), dict(globals(), **locals()))

# --------------------------------------------------------------------------------------------------

# 半角と全角の入力を間違えた際、入力モードの切り替えと入力文字の変換を行う
if 0:
    exec(readConfigExtension(r"zenkaku_hankaku\config.py"), dict(globals(), **locals()))

# --------------------------------------------------------------------------------------------------

# MinTTY を起動するキーを指定する
if 1:
    exec(readConfigExtension(r"mintty\config.py"), dict(globals(), **locals()))

# --------------------------------------------------------------------------------------------------

# MinGW Emacs を起動するキーを指定する
if 0:
    exec(readConfigExtension(r"mingw_emacs\config.py"), dict(globals(), **locals()))

