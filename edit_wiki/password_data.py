import json

def api_login_data(index = 'api_password'):
    with open('secret.json') as f:
        data = json.load(f)
        username = data[index]['username']
        password = data[index]['password']
        return {'user': username, 'password': password}
    # https://wiki.openstreetmap.org/wiki/Special:BotPasswords

def username(index = 'api_password'):
    # https://en.wikipedia.org/wiki/Wikipedia:Naming_conventions_(technical_restrictions)#Restrictions_on_usernames
    with open('secret.json') as f:
        data = json.load(f)
        username = data[index]['username']
        if "@" in username:
            return username.split("@")[0]
        else:
            return username
