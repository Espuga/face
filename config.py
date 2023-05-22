# Importar llibreries
import cv2

global files_path 
files_path = ".\\fotos"

cap = None
estat = True

def cargar():
    global cap, estat
    estat = True
    print("Cargant...")
    cap = cv2.VideoCapture(0)
    estat = False
    print("Cargat")