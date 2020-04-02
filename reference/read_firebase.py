#reading the data
from firebase import firebase

firebase = firebase.FirebaseApplication("https://llllll-93e48.firebaseio.com/registration",None)
result = firebase.get("llllll-93e48/Student","")
print(result)
