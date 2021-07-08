import requests

URL= "https://raw.githubusercontent.com/berandal666/Passwords/master/1337speak.txt"


                          #r <-- read only
                          #w <-- overwrite
                          #a <-- append to the end
with open("passwords.txt","w") as passtxt:
    print(requests.get(URL).text, file=passtxt)

