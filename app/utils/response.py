"""
Response Helper
:author Irfan Andriansyah <irfanandriansyah10@gmail.com>
"""

from flask import jsonify

def responseAPIHelper(item: dict, isSuccess=False) -> dict:
    """
    Generate response client
    :param item: dict
    :param isSuccess: boolean
    """
    return jsonify({
        **item,
        'status': isSuccess
    })
