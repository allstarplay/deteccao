import cv2
import os
from app.configs import config


def test_path_falha():
    os.environ['PATH_VIDEO'] = ''
    p = os.environ['PATH_VIDEO']
    assert p == '' or None

def test_path_camera_sucesso():    
    path = r'C:\Users\george\Desktop\nanascreen\deteccao\video\videoteste.mp4'
    assert config.path_video == path
    
def test_video_sucesso():
    while True:
        vd = cv2.VideoCapture(config.path_video)
        camera, frame = vd.read()
        
        assert camera == True
        assert frame.size > 1
            
        if camera == True and frame.size > 1:
            break

    cv2.destroyAllWindows()

            
def test_video_falha():
    while True:
        vd = cv2.VideoCapture('config.path_video')
        camera, frame = vd.read()
        
        assert camera == False
        assert frame == None
            
        
        if camera == False and frame == None:
            break

    cv2.destroyAllWindows()

test_video_falha()
