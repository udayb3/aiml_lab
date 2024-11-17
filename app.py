from flask import Flask as flask, jsonify, request, render_template
from werkzeug.utils import secure_filename
from flask_cors import CORS
import os
from caption_generate import *
from translation import *
from spConverter import *

ALLOWED_EXTENSIONS = set(['jpg', 'png', 'jpeg' ])
UPLOAD_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Downloads'))

app = flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 100 * 1000 * 1000  # 100 MB of file size 
app.config['CORS_HEADER'] = 'application/json'

def allowedFile(filename):
  return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/uploads', methods=['POST', 'GET'])
def uploaded_file():
  if request.method == 'POST':
    img_file = request.files['file']; lan= request.form['language']
    filename = secure_filename(img_file.filename)
    if allowedFile(filename):
      img_path= os.path.join(app.config['UPLOAD_FOLDER'], filename)
      img_file.save(img_path)

      # using models to generate caption and translate it
      msg= get_caption(img_path); trans_msg= translation(msg, lan)
      file_path= text_to_speech(trans_msg, filename, lan)

      img_path = "./static/images/"+filename; img_file.save(img_path)
      return render_template('upload.html', message=trans_msg, img_path= "files/" + filename, audio_path= file_path)
    else:
      msg = "File type not allowed"
      return render_template('upload.html', message=msg, img_path= "./static/images/"+filename)

@app.route('/', methods=['GET'])
def home():
  return render_template('index.html')

if(__name__=="__main__"):
  app.run(debug=True)