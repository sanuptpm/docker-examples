import os
from flask import Flask, request, jsonify
import os.path

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
        return jsonify({'error': str(e),
                        'status': 500,
                        'message': 'Somthing went wrong'})


@app.route('/files', methods=['POST'])
def create_file():
    try:
        request_data = request.get_json()
        try:
            name = request_data['name']
            data = request_data['data']
            name_of_file = name + '.txt'
        except Exception as e:
            return jsonify({
                'error': str(e),
                'status': 400,
                'message': 'Invaild input/ empty value'})
        if not name or not data:
            return jsonify({
                'status': 400,
                'message': 'Invaild input/ empty value'})
        else:
            # go to test folder
            filepath = os.path.join('/opt/test', name_of_file)
            if not os.path.exists('/opt/test'):
                os.umask(0)
                os.makedirs('/opt/test', mode=0o777)
            os.chdir('/opt/test')
            # check file exist
            if os.path.isfile(name_of_file):
                return jsonify({
                    'name': name_of_file,
                    'status': 409,
                    'message': 'file name already exist'})
            else:
                try:
                    f = open(filepath, "w")
                   # raise Exception("errrrrrrrrrrrrrrrrrrrr")
                    f.writelines([data])
                except Exception as e:
                    raise Exception(str(e))
                finally:
                    print("-------in finally---------------")
                    f.close()
                return jsonify({
                    'name': name_of_file,
                    'status': 200,
                    'message': 'successfully created'})
        

    except Exception as e:
        return jsonify({'error': str(e),
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
        return jsonify({'error': str(e),
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
        return jsonify({'error': str(e),
                        'status': 500,
                        'message': 'Somthing went wrong'})


@app.route('/files/<string:name>', methods=['DELETE'])
def delete_file(name):
    try:
        os.chdir('/opt/test')
        file = os.path.exists(name+".txt")
        try:
            if not file:
                return jsonify({
                    'name': name + ".txt",
                    'status': 404,
                    'message': 'file not exist'})
            else:
                os.remove(name+".txt")
                return jsonify({
                    'id': name,
                    'status': 200,
                    'message': 'successfully deleted'})

        except Exception as e:
            return jsonify({'error': str(e),
                            'status': 404,
                            'message': 'Somthing went wrong'})

    except Exception as e:
        return jsonify({'error': str(e),
                        'status': 500,
                        'message': 'Somthing went wrong'})


@app.route('/files/<string:name>', methods=['PATCH'])
def patch_file(name):
    try:
        os.chdir('/opt/test')
        file = os.path.exists(name+".txt")
        request_data = request.get_json()
        try:
            rename = request_data['name']
            if not file:
                return jsonify({
                    'name': name + ".txt",
                    'status': 404,
                    'message': 'file not exist'})
            else:
                os.rename(name + ".txt", rename+".txt")
                return jsonify({
                    'id': name,
                    'status': 200,
                    'message': 'successfully updated file name'})

        except Exception as e:
            return jsonify({'error': str(e),
                            'status': 404,
                            'message': 'Somthing went wrong'})

    except Exception as e:
        return jsonify({'error': str(e),
                        'status': 500,
                        'message': 'Somthing went wrong'})


@app.route('/files/<string:name>', methods=['PUT'])
def update_file(name):
    try:
        os.chdir('/opt/test')
        file = os.path.exists(name+".txt")
        request_data = request.get_json()
        try:
            data = request_data['data']
            if not file:
                return jsonify({
                    'name': name + ".txt",
                    'status': 404,
                    'message': 'file not exist'})
            else:
                f = open(name + ".txt", "w")
                f.write(data)
                f.close()
                return jsonify({
                    'id': name,
                    'status': 200,
                    'message': 'successfully updated'})

        except Exception as e:
            return jsonify({'error': str(e),
                            'status': 404,
                            'message': 'Somthing went wrong'})

    except Exception as e:
        return jsonify({'error': str(e),
                        'status': 500,
                        'message': 'Somthing went wrong'})
