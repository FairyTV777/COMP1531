import sys

MESSAGE_LIST = []

def authorise(function):
    def wrapper(*args, **kwargs):
        auth_token = args[0]
        if auth_token != "CrocodileLikesStrawberries":
            raise ValueError("Invalid authentication")
        return function(*args, **kwargs)
    return wrapper


@authorise
def get_messages(auth_token):
    return MESSAGE_LIST

@authorise
def add_messages(auth_token, msg):
    global MESSAGE_LIST
    MESSAGE_LIST.append(msg)

if __name__ == '__main__':
    auth_token = ""
    if len(sys.argv) == 2:
        auth_token = sys.argv[1]

    add_messages(auth_token, "Hello")
    add_messages(auth_token, "How")
    add_messages(auth_token, "Are")
    add_messages(auth_token, "You?")
    print(get_messages(auth_token))