"""
Extract Video
@author Irfan Andriansyah <irfan@99.co>
"""
import os
import cv2
import imutils
from app.modules.compression_modules import CompressModules


class ExtractVideoModules:
    """
    Extract Video
    """

    VIDEO_PATH = ''
    CAPTURE = None
    FRAME = 1
    IMAGE_ARRAY = []

    def __init__(self):
        """
        Constructor
        """

        self.VIDEO_PATH = os.path.abspath(os.getcwd()) + '/upload/video-sample.mp4'
        self.CAPTURE = cv2.VideoCapture(self.VIDEO_PATH)
 
    
    def get_path(self, type_path, index):
        image = 'extract-frame-' + str(index) + '.jpg'
        if type_path == 'image':
            return image

        return os.path.abspath(os.getcwd()) + '/upload/' + image

    def extract_frame(self):
        while(self.CAPTURE.isOpened()):
            ret, frame = self.CAPTURE.read()
            if ret == False:
                break
            cv2.imwrite(self.get_path('path', self.FRAME),frame)
            self.FRAME+=1
        
        self.CAPTURE.release()
        cv2.destroyAllWindows()

    def make_video(self):
        img_array = []
        for index in range(1, self.FRAME):
            if index % 2 == 1:
                continue

            image = 'compress-image-extract-frame-' + str(index) + '.jpg'
            img = cv2.imread(
                os.path.abspath(os.getcwd()) + '/upload/' + image
            )
            resized = imutils.resize(img, width=720)
            img = imutils.resize(resized, width=1080)
            img = cv2.GaussianBlur(img, (5,5), 0)
            height, width, layers = img.shape
            size = (width,height)
            img_array.append(img)

        out = cv2.VideoWriter(
            'project.avi',
            cv2.VideoWriter_fourcc(*'DIVX'),
            12,
            size
        )

        for i in range(len(img_array)):
            out.write(img_array[i])
        
        out.release()

    
    def compress_frame(self):
        for index in range(1, self.FRAME):
            if index % 2 == 1:
                continue
            else:
                compress = CompressModules(self.get_path('image', index))
            compress.saveImage()

    def run(self):
        self.extract_frame()
        self.compress_frame()
        self.make_video()