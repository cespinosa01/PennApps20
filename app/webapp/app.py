#!/usr/bin/python
import boto3
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    imageFile='example_04.jpg'
    client=boto3.client('rekognition')

    with open(imageFile, 'rb') as image:
        response = client.detect_labels(Image={'Bytes': image.read()})

    print('x ' + imageFile)
    #for label in response['Labels']:
    #    labels= (label['Name'] + ' : ' + str(label['Confidence']))
    #    print(str(labels))
    
    return render_template('index2.html', labels=response['Labels'])

if __name__ == '__main__':
     app.run()
