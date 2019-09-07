#!/usr/bin/python
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
@app.route("/")
def index():
    imageFile='apple.jpg'
    client=boto3.client('rekognition')

    with open(imageFile, 'rb') as image:
        response = client.detect_labels(Image={'Bytes': image.read()})
    d = {}
    for label in response['Labels']:
    #print('x ' + imageFile)
        query = label['Name']
        recipes= search(query, tld="co.in", num=10, stop=1, pause=2)
        d[query]=list(recipes)

    return render_template('index2.html', labels=response['Labels'], d=d)

if __name__ == '__main__':
     app.run()
