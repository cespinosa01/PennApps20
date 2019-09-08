#!/usr/bin/python
#this file uses aws, flask, python, and googlesearch
import boto3
from flask import Flask, render_template, request
from googlesearch import search
from banana.classify_images_01 import banana_function
from potatoes.classify_images_02 import potato_function
from apple.classify_images_03 import apple_function
from bread.classify_images_04 import bread_function

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
        #if(label == "Food"):
            #banana_function("knn","3scenes","3scenes/ripe_new/ripe_01.jpg")
        #elif(label == "Apple"):
            #potato_function("knn","3scenes","3scenes/ripe_new/ripe_01.jpeg")
        #elif(label == "Fruit"):
            #apple_function("knn","3scenes", "3scenes/ripe_new/ripe_01.jpeg")
        #elif(label == "Plant"):
            #bread_function("knn","3scenes", "3scenes/bread/bread_01.jpg")
        #else:
            #print("Food")
        return render_template('index9.html', labels=response['Labels'], d=d)
    else:
        return render_template('index7.html')

if __name__ == '__main__':
     app.run()
