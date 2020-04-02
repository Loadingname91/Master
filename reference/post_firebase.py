# storing the data
from firebase import firebase as fb_inst


def post_data(data, fb_inst):
    fb_inst = fb_inst.FirebaseApplication("https://llllll-95e48.firebaseio.com/registration", None)
    result = fb_inst.post("llllll-93e48/Student", data)
    if result :
        return result
    else :
        return "error in forwarding "+ result
