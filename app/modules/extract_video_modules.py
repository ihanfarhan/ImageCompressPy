"""
Extract Video
@author Irfan Andriansyah <irfan@99.co>
"""
import os
import cv2
from app.modules.compression_modules import CompressModules


class ExtractVideoModules:
    """
    Extract Video
    """

    VIDEO_PATH = ''
    CAPTURE = None
    FRAME = 1

    def __init__(self):
        """
        Constructor
        """

        self.VIDEO_PATH = os.path.abspath(os.getcwd()) + '/upload/video-sample.mp4'
        self.CAPTURE = cv2.VideoCapture(self.VIDEO_PATH)
    
    def get_path(self):
        return os.path.abspath(os.getcwd()) + '/upload/extract-frame-' + str(self.FRAME) + '.jpg'

    def extract_frame(self):
        while(self.CAPTURE.isOpened()):
            ret, frame = self.CAPTURE.read()
            if ret == False:
                break
            cv2.imwrite(self.get_path(),frame)
            self.FRAME+=1
        
        self.CAPTURE.release()
        cv2.destroyAllWindows()
    
    def compress_frame(self):
        for index in range(self.FRAME):
            CompressModules
            print(index)

    def run(self):
        self.extract_frame()
        self.compress_frame()