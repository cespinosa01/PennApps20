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
@app.route("/")
def index():
    imageFile='banana_01.jpg'
    client=boto3.client('rekognition')

    with open(imageFile, 'rb') as image:
        response = client.detect_labels(Image={'Bytes': image.read()})
    d = {}
    #print('x ' + imageFile)
    label = response['Labels'][0]['Name']
    query = label + " recipe"
    recipes= search(query, tld="co.in", num=10, stop=1, pause=2)
    d[label]=list(recipes)
    label = response['Labels'][0]['Name']
    print(label)
    if(label) == "banana":
        classify_images()
    return render_template('index2.html', labels=response['Labels'], d=d)

if __name__ == '__main__':
     app.run()
