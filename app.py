import eel
from back.classes.Users import Dispatcher, Client

eel.init('front')

@eel.expose
def create_user(role, *args):
    if role == "Dispatcher":
        user = Dispatcher(*args)
    elif role == "Client":
        user = Client(*args)
    else:
        # Handle invalid role
        return None
    return user

@eel.expose
def open_window(role):
    if role == "Dispatcher":
        eel.spawn('dispatcher.html')
    elif role == "Client":
        eel.spawn('client.html')

eel.start('index.html', size=(750, 650))