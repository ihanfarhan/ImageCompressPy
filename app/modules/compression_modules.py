"""
Compress Module
@author Irfan Andriansyah <irfan@99.co>
"""
import os
from app import photos
from string import Template
from PIL import Image, ImageFilter


class CompressModules:
    """
    Blur Module
    """

    DEFAULT_IMAGE = ''
    IMAGE = ''
    BACKGROUND = None

    def __init__(self, images):
        """
        Constructor
        :param images: Str
        """
        self.DEFAULT_IMAGE: str = images
        self.IMAGE: str = os.path.abspath(os.getcwd()) + '/upload/' + images
        self.BACKGROUND = self.setterBackground()
    
    def setterBackground(self):
        """
        Setter background image
        """
        return Image.open(self.IMAGE)

    
    def setterPath(self):
        base_filename = os.path.basename(self.IMAGE)
        template = Template('compress-image-$base_filename')
        path = template.substitute(base_filename=base_filename)

        return {
            "path": path,
            "full_path": os.path.abspath(os.getcwd()) + '/upload/' + path,
        }

    def saveImage(self):
        basewidth = 720
        wpercent = (basewidth / float(self.BACKGROUND.size[0]))
        hsize = int((float(self.BACKGROUND.size[1]) * float(wpercent)))
        self.BACKGROUND = self.BACKGROUND.resize((basewidth,hsize), Image.ANTIALIAS)
        self.BACKGROUND.save(
            self.setterPath().get('full_path'),
            optimize=True,
            quality=0
        )
    
    def run(self):
        self.saveImage()

        return {
            "original_image": photos.url(self.DEFAULT_IMAGE),
            "compress_image": photos.url(self.setterPath().get('path')),
            "original_image_size": round(os.stat(self.IMAGE).st_size / 1024, 2),
            "compress_image_size": round(os.stat(self.setterPath().get('full_path')).st_size / 1024, 2)
        }
