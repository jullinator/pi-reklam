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
