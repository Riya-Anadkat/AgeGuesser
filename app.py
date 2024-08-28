import cv2
import base64
from flask import Flask, render_template, request, jsonify
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from dotenv import load_dotenv
import random
import numpy as np
import os
import io
import time
import requests

load_dotenv()


app = Flask(__name__)


app.config['KEY'] = os.environ.get('VISION_KEY')
app.config['ENDPOINT'] = os.environ.get('VISION_ENDPOINT')

face_client = FaceClient(app.config['ENDPOINT'], CognitiveServicesCredentials(app.config['KEY']))

# def detect_age(image_path):
#     h
def capture_image_from_camera_detect_age():

    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return
    
    ret, frame = cap.read()
    
    if not ret:
        print("Error: Could not capture frame.")
        return
    
    image_file = f"image.jpg" 
    cv2.imwrite(image_file, frame)
    print(f"Image captured and saved as '{image_file}'")
    
    cap.release()

    url = "https://age-detector.p.rapidapi.com/age-detection"

    payload = { "url": "image.jpg" }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "684172fe98msh67e7acd932504a9p1d161bjsn3e5443e58cc6",
        "X-RapidAPI-Host": "age-detector.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.json())


    return True

while True:
    capture_image_from_camera_detect_age()
    time.sleep(30)


@app.route('/random_num', methods=['GET'])
def random_num():
   return random.randint(0,100)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)