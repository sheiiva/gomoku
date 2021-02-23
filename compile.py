#
# A Python script to generate .exe from  python project - Gomoku.
#
# (02/05/2021) - Barcelona
# Authors:  Corentin COUTRET-ROZET <corentin.rozet@epitech.eu>
#           Maxence DESROUSSEAUX <maxence.desrousseaux@epitech.eu>
#           Hugo LACKAR <hugo1.lachkar@epitech.eu>
#

from os import system


files =  [
    "deps\\__init__.py",
    "deps\\infos.py",
    "sources\\algorithm\\__init__.py",
    "sources\\algorithm\\AIMove.py",
    "sources\\commands\\__init__.py",
    "sources\\commands\\About.py",
    "sources\\commands\\Begin.py",
    "sources\\commands\\Board.py",
    "sources\\commands\\End.py",
    "sources\\commands\\Info.py",
    "sources\\commands\\Start.py",
    "sources\\commands\\Turn.py",
    "sources\\utils\\__init__.py",
    "sources\\utils\\definitions.py",
    "sources\\utils\\Log.py",
    "sources\\utils\\tools.py",
    "sources\\Game.py",
    "sources\\GameBoard.py",
    "sources\\main.py"
]

files_list = ""
for file in files:
    files_list += " " + file

system("pip install pyinstaller")
system("pyinstaller" + files_list + " --name pbrain-gomoku-ai.exe --onefile")
system('copy .\\dist\\pbrain-gomoku-ai.exe .')