import firebase

db = firebase.database()
def stream_handler(message):
    print(message["event"]) # put
    print(message["path"]) # /-K7yGTTEp7O549EzTYtI
    print(message["data"][1]) # {'title': 'Pyrebase', "body": "etc..."}

my_stream = db.child("computers").stream(stream_handler)
