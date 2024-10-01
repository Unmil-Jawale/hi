import os
import eel

eel.init("Front")

os.system('start msedge.exe --app="http://127.0.0.1:5500/Jarvis/Front/Index.html"')

eel.start('index.html', mode=None, host="localhost", block=True)

