import os
from flask import Flask, request, jsonify
import datetime
import os.path
import json

import fnmatch

app = Flask(__name__)

SECRET_KEY = os.environ.get("SECRET_KEY")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=4000)


@app.route("/")
def hello():
    return "Flask inside Docker!! Hello"


@app.route("/env")
def evnshow():
    try:
        if SECRET_KEY:
            return "Remote address : " + SECRET_KEY
        else:
            return 'Remote address not set'
    except Exception as e:
        return jsonify({'error': e,
                        'status': 500,
                        'message': 'Somthing went wrong'})


# {
#     "message": "Invaild input/ empty value",
#     "status": 400
# }
#  http://127.0.0.1:5000/files
@app.route('/files', methods=['POST'])
def create_file():
    try:
        request_data = request.get_json()
        name = request_data['name']
        data = request_data['data']
        name_of_file = name + '.txt'
        if name and data:
            # go to test folder
            filepath = os.path.join('/opt/test', name_of_file)
            if not os.path.exists('/opt/test'):
                os.umask(0)
                os.makedirs('/opt/test', mode=0o777)
            os.chdir('/opt/test')
            # check file exist
            if os.path.isfile(name_of_file):
                print("file does exist at this time")
                return jsonify({
                    'name': name_of_file,
                    'status': 409,
                    'message': 'file name already exist'})
            else:
                f = open(filepath, "w")
                f.writelines([data])
                f.close()
                return jsonify({
                    'name': name_of_file,
                    'status': 200,
                    'message': 'successfully created'})
        else:
            return jsonify({
                'status': 400,
                'message': 'Invaild input/ empty value'})

    except Exception as e:
        return jsonify({'error': e,
                        'status': 500,
                        'message': 'Somthing went wrong'})


@app.route('/files', methods=['GET'])
def get_files_count():
    try:
        os.chdir('/opt/test')
        count = str(len(fnmatch.filter(os.listdir(), '*.txt')))
        return jsonify({
            'count': count,
            'status': 200,
            'message': 'successfully listed'})
    except Exception as e:
        return jsonify({'error': e,
                        'status': 500,
                        'message': 'Somthing went wrong'})

@app.route('/files/<string:name>', methods=['GET'])
def get_file_name(name):
    try:
        return jsonify({
            'id': name,
            'status': 200,
            'message': 'successfully listed'})
    except Exception as e:
        return jsonify({'error': e,
                        'status': 500,
                        'message': 'Somthing went wrong'})

@app.route('/files/<string:name>', methods=['DELETE'])
def delete_file(name):
    try:
        return jsonify({
            'id': name,
            'status': 200,
            'message': 'successfully deleted'})
    except Exception as e:
        return jsonify({'error': e,
                        'status': 500,
                        'message': 'Somthing went wrong'})

@app.route('/files/<string:name>', methods=['PATCH'])
def patch_file(name):
    try:
        return jsonify({
            'id': name,
            'status': 200,
            'message': 'successfully updated'})
    except Exception as e:
        return jsonify({'error': e,
                        'status': 500,
                        'message': 'Somthing went wrong'})

@app.route('/files/<string:name>', methods=['PUT'])
def update_file(name):
    try:
        return jsonify({
            'id': name,
            'status': 200,
            'message': 'successfully updated'})
    except Exception as e:
        return jsonify({'error': e,
                        'status': 500,
                        'message': 'Somthing went wrong'})

