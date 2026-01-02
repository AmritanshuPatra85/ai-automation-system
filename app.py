import sys
import importlib

print("RUNNING app.py FROM:", __file__)

# Clear the cache
if 'automations' in sys.modules:
    importlib.reload(sys.modules['automations'])

from flask import Flask, render_template, request, jsonify
from automations import organize_by_file_type, bulk_rename

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/organize', methods=['POST'])
def organize():
    folder_path = request.form.get('folder_path')
    
    if not folder_path:
        return jsonify({
            'success': False,
            'message': 'Please provide a folder path'
        })
    
    result = organize_by_file_type(folder_path)
    return jsonify(result)

@app.route('/rename', methods=['POST'])
def rename():
    folder_path = request.form.get('folder_path')
    prefix = request.form.get('prefix')
    
    if not folder_path or not prefix:
        return jsonify({
            'success': False,
            'message': 'Please provide both folder path and prefix'
        })
    
    result = bulk_rename(folder_path, prefix)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)