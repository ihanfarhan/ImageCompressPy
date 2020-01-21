"""
Compress Image enpoint api
:author Irfan Andriansyah <irfanandriansyah10@gmail.com>
"""
import os
from app import photos
from app.utils.response import responseAPIHelper
from flask import Blueprint, request, send_from_directory
from app.modules.compression_modules import CompressModules


mod = Blueprint('blur', __name__, url_prefix='/compress')

html = ''.join([
    '''
    <!DOCTYPE html>
    <title>Upload File</title>
    <h1>Photo Upload</h1>
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
    <link
        href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
        rel="stylesheet"
        integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
        crossorigin="anonymous"
    >
    <form method=post enctype=multipart/form-data>
         <input type=file name=photo class="form-control">
         <button type=submit class="btn btn-primary">
            Upload
         </button>
    </form>
    '''
])


@mod.route('/api', methods=['POST'])
def upload_images():
    try:
        if request.method == 'POST' and 'photo' in request.files:
            filename = photos.save(request.files['photo'])
            compress_image = CompressModules(filename).run()

            return responseAPIHelper(compress_image, True), 200
        else:
            raise ValueError('Error Request')
    except BaseException as e:
        return responseAPIHelper({
            'Error': str(e)
        }, False), 200


@mod.route('/', methods=['GET', 'POST'])
def form_upload():
    try:
        if request.method == 'POST' and 'photo' in request.files:
            filename = photos.save(request.files['photo'])
            compress_image = CompressModules(filename).run()

            return ''.join([
                html,
                '<div class="form-media">',
                '   <div class="form-media__item">',
                '       <img src=' + compress_image.get('compress_image') + '>',
                '       <h5>' + str(compress_image.get('compress_image_size')) + 'Kb</h5>',
                '   </div>',
                '   <div class="form-media__item">',
                '       <img src=' + compress_image.get('original_image') + '>',
                '       <h5>' + str(compress_image.get('original_image_size')) + 'Kb</h5>',
                '   </div>',
                '''<link href="''' + request.host_url + '''compress/asset/style.css" rel='stylesheet'>'''
            ])
        else:
            return ''.join([
                html,
                '''<link href="''' + request.host_url + '''compress/asset/style.css" rel='stylesheet'>'''   
            ])
    except BaseException as e:
        return responseAPIHelper({
            'Error': str(e)
        }, False), 200

@mod.route('/asset/<path:path>')
def send_js(path):
    return send_from_directory('asset', path)