import cv2 
from matplotlib import pyplot
from mtcnn.mtcnn import MTCNN
import config
import os

def normalize_image(image):
    # Converitr la image a escala de grisos
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Aplicar la normalització de brillo i contrast
    normalized = cv2.normalize(gray, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
    # Convertir la imatge a RGB
    normalized = cv2.cvtColor(normalized, cv2.COLOR_GRAY2BGR)
    return normalized
def comprovar(img_log, user):
    cv2.imwrite(config.files_path+"\\current\\"+user+'_LOG.jpg', img_log)
    def reg_face(img, list_results):
        data = pyplot.imread(img)
        for i in range(len(list_results)):
            # Obtenir cordenades
            x1, y1, ample1, alçada1 = list_results[i]['box']
            x2, y2 = x1 + ample1, y1 + alçada1
            # Definir el subplot
            pyplot.subplot(1, len(list_results), i+1)
            pyplot.axis('off')
            face_reg = data[y1:y2, x1:x2]
            face_reg = cv2.resize(face_reg, (150,200), interpolation=cv2.INTER_CUBIC)   # Guardar la imatge 
            cv2.imwrite(config.files_path+"\\current\\"+user+'_LOG.jpg', face_reg)
            #Plotejem les cares
            pyplot.imshow(data[y1:y2, x1:x2])
        pyplot.show(block=False)
        pyplot.close()
    img = config.files_path+"\\current\\"+user+"_LOG.jpg"
    pixels = pyplot.imread(img)
    detector = MTCNN()
    faces = detector.detect_faces(pixels)
    reg_face(img, faces)
    def orb_sim(img1, img2):
        orb = cv2.ORB_create()  # Crear el objecte de comparació
        # Extreu punts clau de img1 i img2
        kpa, descr_a = orb.detectAndCompute(img1, None)
        kpa, descr_b = orb.detectAndCompute(img2, None)
        comp = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)   # Crear el comparador de força
        matches = comp.match(descr_a, descr_b)      # Aplicem el comparador als descriptors
        similar_regions = [i for i in matches if i.distance < 70]   # Extreu les regions similars en base als punts clau
        if len(matches) == 0:
            return 0
        return len(similar_regions)/len(matches)
    im_files = os.listdir(os.path.join(os.getcwd(), 'fotos'))     # Llistar els arxius de la carpeta fotos
    if user in im_files:
        face_log = cv2.imread(config.files_path+"\\current\\"+user+"_LOG.jpg",0)
        for image in os.listdir(config.files_path+"\\"+user):
            print("====================")
            face_reg = cv2.imread(config.files_path+"\\"+user+"\\"+image.split(".")[0]+".jpg",0)
            similar = orb_sim(face_reg, face_log)
            print("Compatibility", image.split(".")[0]+": " + str(round(similar, 2)))
            if similar >= 0.9:
                os.remove(config.files_path+"\\current\\"+user+"_LOG.jpg")
                print("Welcome into the system")
                result = ["Log In SUCCESFULLY\n Compatibility: "+str(round(similar*100, 2))+"%", "green", "si", "true"]
                return result
        else:
            print("Bad face")
            os.remove(config.files_path+"\\current\\"+user+"_LOG.jpg")
            result = ["Log In FAILED\n Compatibility: "+str(round(similar*100, 2))+"%", "red", "si", "false"]
            return result
    else:
        print("User not found")
        os.remove(config.files_path+"\\current\\"+user+"_LOG.jpg")
        result = ["User not found", "red", "si", "false"]
        return result
    
cap = None

def cargar():
    global cap, estat
    print("Cargant...")
    cap = cv2.VideoCapture(0)
    print("Cargat")
    #Actualitzar



def login(user, cargar):
    #cap = cv2.VideoCapture(0)
    while True:
        ret,frame = cap.read()
        if frame is not None and frame.shape[0] > 0 and frame.shape[1] > 0:
            cv2.imshow('FaceID',frame)
            cap.release()
            cv2.destroyAllWindows()
            return comprovar(normalize_image(frame), user)