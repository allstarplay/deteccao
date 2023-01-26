import cv2
from configs import config

class Camera:
    
    vd = cv2.VideoCapture(config.path_video)
        
    def video(vd):    
            while True:
                camera, frame = vd.read()
                    
                cv2.imshow('frame', frame)
                
                if cv2.waitKey(1) == ord('q'):
                    break

            vd.release()
            cv2.destroyAllWindows()

    video(vd)


 
   
        
