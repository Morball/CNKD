import urllib.request
import ctypes
import os
FILENAME="CNKD.jpeg"
ROOT_PATH=os.path.expanduser("~")

def UpdateDesktopBackground(url):
    path=f"{ROOT_PATH}\\Desktop"
    if os.path.isfile(os.path.join(path, FILENAME)):
        os.remove(os.path.join(path, FILENAME))

    urllib.request.urlretrieve(url, os.path.join(path, FILENAME))
    ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.join(path, FILENAME) , 0)


def MessageBox(title, message):
    return ctypes.windll.user32.MessageBoxW(0, message, title, 0)

