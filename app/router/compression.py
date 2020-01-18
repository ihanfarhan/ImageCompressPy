"""
Compress Image enpoint api
:author Irfan Andriansyah <irfanandriansyah10@gmail.com>
"""
import os
from app import photos
from flask import Blueprint, request
from app.utils.response import responseAPIHelper
from app.modules.compression_modules import CompressModules


mod = Blueprint('blur', __name__, url_prefix='/blur')

@mod.route('/', methods=['POST'])
def upload_images():
    try:
        if request.method == 'POST' and 'photo' in request.files:
            filename = photos.save(request.files['photo'])
            file_url = photos.url(filename)
            compress_image = CompressModules(filename).run()

            return responseAPIHelper(compress_image, True), 200
        else:
            raise ValueError('Error Request')
    except BaseException as e:
        print(e)
        return responseAPIHelper({
            'Error': str(e)
        }, False), 200