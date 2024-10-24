API_KEY = ''
PACKAGE_NAME = 'ai4thai-lib'
def get_api_key():
    return API_KEY

def set_api_key(new_key):
    global API_KEY
    API_KEY = new_key
