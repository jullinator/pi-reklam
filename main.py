from firebase import firebase

db = firebase.database()
spots = db.child("spots")



all_spots = spots.order_by_child("computer").equals_to("computer1").get()

for spot in all_spots.each():
    print(spot.val())



#def stream_handler(message):
#    print(message["event"]) # put
#    print(message["path"]) # /-K7yGTTEp7O549EzTYtI
#    print(message["data"]) # {'title': 'Pyrebase', "body": "etc..."}
