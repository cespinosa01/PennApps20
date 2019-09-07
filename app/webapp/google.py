from googlesearch import search
from flask import Flask, render_template
import boto3
app = Flask(__name__)
# to search
@app.route("/")
def index():
    imageFile='apple.jpg'
    client=boto3.client('rekognition')

    with open(imageFile, 'rb') as image:
        response = client.detect_labels(Image={'Bytes': image.read()})

    print('x ' + imageFile)

    return render_template('index2.html', labels=response['Labels'])
    query = response['Labels']
    print(str(query))
    #for j in search(query, tld="co.in", num=10, stop=1, pause=2):
        #print(j)

if __name__ == '__main__':
     app.run()
