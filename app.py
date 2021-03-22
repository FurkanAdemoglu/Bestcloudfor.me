
from flask import  Flask
from flask import  request,jsonify,abort
import json
import requests
webhook_url="https://webhook.site/b5a95f14-1201-49ff-a14d-56f04b40bd3f"
app=Flask(__name__)
names= {
        'firstname':'Furkan',
        'lastname':'Ademoglu'
    },




@app.route("/")
def home():
    return jsonify(names)
@app.route("/whoami",methods= ['GET'])
def whoami():
    firstname=request.args.get('firstname')
    lastname=request.args.get('lastname')
    names_2={
        'firstname':firstname,
        'lastname':lastname
    }
    return jsonify(names_2)


@app.route("/alert",methods=['GET', 'POST','DELETE', 'PATCH'])
def alert():
    message={
        "message":"The method is not allowed for the requested URL."
    }
    if request.method!='POST':
        return jsonify(message)
    else:
        data=request.get_json()
        firstname=data['firstname']
        lastname=data['lastname']
        names_3={
            'firstname':firstname,
            'lastname':lastname
        }


        requests.post(webhook_url,data=json.dumps(names_3),headers={'Content-Type':'application/json'})

