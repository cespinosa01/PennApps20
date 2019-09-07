#!/usr/bin/python
import boto3
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    imageFile='apple.jpg'
    client=boto3.client('rekognition')

    with open(imageFile, 'rb') as image:
        response = client.detect_labels(Image={'Bytes': image.read()})

    print('x ' + imageFile)

    return render_template('index2.html', labels=response['Labels'])

if __name__ == '__main__':
     app.run()
