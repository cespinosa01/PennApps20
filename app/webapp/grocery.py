#!/usr/bin/python
#this file uses aws, flask, python, and googlesearch
import boto3
from flask import Flask, render_template, request
from googlesearch import search

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def generate_list_recipies(recipes):
    l=[]
    for i in range(1,11):
        x=next(recipes)
        l.append(x)
    return l
@app.route('/first/', methods=['GET', 'POST'])
def first():
    if request.method == "POST":
        print(request.form)
        print(request.files)
        image = request.files["picture"]
        bucket='bucket'
        photo=image

        client=boto3.client('rekognition')
        response = client.detect_text(Image={'Bytes': image.read()})
        textDetections=response['TextDetections']
        print ('Detected text')
        for text in textDetections:
            #print ('Detected text:' + text['DetectedText'])
            #print ('Confidence: ' + "{:.2f}".format(text['Confidence']) + "%")
            #print ('Id: {}'.format(text['Id']))
            #if 'ParentId' in text:
                #print ('Parent Id: {}'.format(text['ParentId']))
                final= 'Type:' + text['Type']
                print(final)
        return render_template('first.html', textDetections=textDetections)
    else:
        return render_template('index8.html')
if __name__ == '__main__':
     app.run()
