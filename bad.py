import cv2
import pyscreenshot 

class Detecta:
    
    webCamera = cv2.VideoCapture(0)
    classificadorVideoFace = cv2.CascadeClassifier('haarcascades/haarcascade_russian_plate_number.xml')

    while True:
    
        camera, frame = webCamera.read()

        cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        detecta = classificadorVideoFace.detectMultiScale(cinza)
        for(x, y, l, a) in detecta:
            cv2.rectangle(frame, (x, y), (x + l, y + a), (255, 0, 0), 2)
        
        try:
            if detecta.size:
             
                print('Placa detectada')
                # aqui chama a função para reconhecer os caracteres
                image = pyscreenshot.grab() 
                image.show() 
                image.save("print.png") 
            
            
        except:
            pass

        cv2.imshow("Video WebCamera", frame)

        if cv2.waitKey(1) == ord('q'):
            break   
        

    webCamera.release()
    cv2.destroyAllWindows()
