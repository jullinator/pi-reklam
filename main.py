from firebase import firebase
import gui

db = firebase.database()
storage = firebase.storage()
spots = db.child("spots")



all_spots = spots.order_by_child("computer").equals_to("computer1").get()

for spotChild in all_spots.each():
    spot = spotChild.val()
    storage.child("images/"+spot["image"]).download("images/"+spot["image"])
    #gui.make_image(spot["image"], spot["image"])

#gui.show_image()


#def stream_handler(message):
#    print(message["event"]) # put
#    print(message["path"]) # /-K7yGTTEp7O549EzTYtI
#    print(message["data"]) # {'title': 'Pyrebase', "body": "etc..."}
