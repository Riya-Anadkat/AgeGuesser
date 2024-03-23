# import cv2
import base64
from flask import Flask, render_template, request, jsonify
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from dotenv import load_dotenv
import numpy as np
import os

load_dotenv()


app = Flask(__name__)


app.config['KEY'] = os.environ.get('VISION_KEY')
app.config['ENDPOINT'] = os.environ.get('VISION_ENDPOINT')

face_client = FaceClient(app.config['ENDPOINT'], CognitiveServicesCredentials(app.config['KEY']))

# def detect_age(image_path):
#     h

def detect_age(frame_data):
    frame_np = np.frombuffer(frame_data, dtype=np.uint8)

    # frame_np = np.array(frame_data, dytpe=np.uint8)
    # _, img_encoded = cv2.imencode('.jpg', frame_np)
    # image_stream = img_encoded.tobytes()
    
    # print(image_stream)
    # detected_faces = face_client.face.detect_with_stream(image=image_stream, recognition_model='recognition_04', return_face_attributes=['age'])

    # if not detected_faces:
    #     print("No faces detected")
    #     return False

    # age = detected_faces[0].face_attribute.age
    # print(f"Estimated age is {age}")
    return True

@app.route('/capture_frame', methods=['POST'])
def capture_frame():
    frame_data_base64 = request.json['frame']
    frame_data = base64.b64decode(frame_data_base64.split(",")[1]) 

    # print(frame_data)
    detect_age(frame_data)
    return jsonify({'message': 'Frame received successfully'})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)