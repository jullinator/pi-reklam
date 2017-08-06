import pyrebase

config = {
    "apiKey": "AIzaSyBHbCmu6XAlxDDcjfZaWh6P4tvoY_EgMMU",
    "authDomain": "pi-reklam.firebaseapp.com",
    "databaseURL": "https://pi-reklam.firebaseio.com",
    "projectId": "pi-reklam",
    "storageBucket": "pi-reklam.appspot.com",
    "messagingSenderId": "460806227224"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
def stream_handler(message):
    print(message["event"]) # put
    print(message["path"]) # /-K7yGTTEp7O549EzTYtI
    print(message["data"][1]) # {'title': 'Pyrebase', "body": "etc..."}

my_stream = db.child("computers/1/images").stream(stream_handler)