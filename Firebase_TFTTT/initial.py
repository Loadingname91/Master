import pyrebase

"""
config file is altered , get you config file from firebase db 

"""

config = {

    "apiKey": "",
    "authDomain": "",
    "databaseURL": "",
    "projectId": "",
    "storageBucket": "",
    "messagingSenderId": "",
    "appId": ""

}

firebase = pyrebase.initialize_app(config)






