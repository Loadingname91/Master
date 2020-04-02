#reading the data
from firebase import firebase

firebase = firebase.FirebaseApplication("https://llllll-93e48.firebaseio.com/registration",None)
result = firebase.put("llllll-93e48/Student/-M3r96GU4KoiGyq7sj_m","phone",9886768539)
print(result)

