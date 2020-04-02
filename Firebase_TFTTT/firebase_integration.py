"""
parameters:  firebase_instance = Firebase instance comming from initial.py
            list_data = data in a list passed to store in the db

returns  : string 'success'

"""
def push_data(firebase_instance,list_data):
    db=firebase_instance.database()
    data={
        "playlist_added_to":list_data[0],
        "song_added":list_data[1],
        "song_artist":list_data[2],
        "song_added_by":list_data[3]
    }
    print(db.child("spotify").push(data))
    return "success"

"""
parameters: firebase_instance = Firebase instance comming from initial.py

returns  : a list containing the pyre objects from the firebase db

"""


def get_data(firebase_instance):
    return firebase_instance.database().child("spotify").get()