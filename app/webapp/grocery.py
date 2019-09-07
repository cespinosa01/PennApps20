#!/usr/bin/python
#this file uses aws, flask, python, and googlesearch
import boto3
from flask import Flask, render_template
from googlesearch import search

app = Flask(__name__)
def generate_list_recipies(recipes):
    l=[]
    for i in range(1,11):
        x=next(recipes)
        l.append(x)
    return l
@app.route("/first")
def first():
    bucket='bucket'
    photo='grocery_list_2.jpeg'

    client=boto3.client('rekognition')

    with open(photo, 'rb') as image:
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
if __name__ == '__main__':
     app.run()
