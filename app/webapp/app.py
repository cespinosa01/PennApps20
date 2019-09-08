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
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        print(request.form)
        print(request.files)
        image = request.files["picture"]

        client=boto3.client('rekognition')

        response = client.detect_labels(Image={'Bytes': image.read()})
        d = {}
        #print('x ' + imageFile)
        label = response['Labels'][0]['Name']
        query = label + " recipe"
        recipes= search(query, tld="co.in", num=10, stop=1, pause=2)
        d[label]=list(recipes)
        label = response['Labels'][0]['Name']
        print(label)
        #if(label) == "banana":
        return render_template('index2.html', labels=response['Labels'], d=d)
    #classify_images()
    else:
        return render_template('index5.html')

if __name__ == '__main__':
     app.run()
