#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To Rana Aahil
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.001)

#Dev:Rana
##### LOGO #####
logo = """
\033[1;96m██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗
\033[1;96m██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝
\033[1;96m██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░
\033[1;96m██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░
\033[1;96m██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗
\033[1;96m╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝

\033[1;92m████████╗██╗░██████╗░███████╗██████╗░
\033[1;92m╚══██╔══╝██║██╔════╝░██╔════╝██╔══██╗
\033[1;92m░░░██║░░░██║██║░░██╗░█████╗░░██████╔╝
\033[1;92m░░░██║░░░██║██║░░╚██╗██╔══╝░░██╔══██╗
\033[1;92m░░░██║░░░██║╚██████╔╝███████╗██║░░██║
\033[1;92m░░░╚═╝░░░╚═╝░╚═════╝░╚══════╝╚═╝░░╚═╝

\033[1;95m┈┈┈╱▔▔▔▔▔▔╲┈╭━━━╮┈┈ Fuck Fb System.
\033[1;95m┈┈▕┈╭━╮╭━╮┈▏┃Sohag┃┈┈
\033[1;97m┈┈▕┈┃╭╯╰╮┃┈▏╰┳━━╯┈┈
\033[1;97m┈┈▕┈╰╯╭╮╰╯┈▏┈┃┈┈┈┈┈ 
\033[1;97m┈┈▕┈┈┈┃┃┈┈┈▏━╯┈┈┈┈┈
\033[1;95m┈┈▕┈┈┈╰╯┈┈┈▏┈┈┈┈┈┈┈
\033[1;95m┈┈▕╱╲╱╲╱╲╱╲▏┈┈┈┈┈┈┈

\033[1;93m▇▇▇▇▇ Facebook\033[1;93m Sohag▇▇▇▇▇
\033[1;97m
                 ⊂ヽ
               　 ＼＼  Λ＿Λ
              　　 ＼(  ˘ω˘  )
                　　　 >　⌒ヽ
                 　　　/ 　 へ＼
                 　　 /　　/　＼＼
                 　　 ﾚ　ノ　　 ヽ_つ
                 　　/　/
                 　 /　/|
                  　(　(ヽ
                  　|　|、＼
                  　| 丿 ＼ ⌒)
                  　| |　　) /
                   ノ )    Lﾉ
                  (_／     　　　
\033[1;97m:•◄►•═ ═ ═ ═ ═ ═ ═ •◄►•\033[1;93mBlackTiger\033[1;97m•◄►•═ ═ ═ ═ ═ ═ ═ •◄►•"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """
\033[1;91m██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗
\033[1;91m██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝
\033[1;93m██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░
\033[1;93m██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░
\033[1;92m██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗
\033[1;92m╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝

\033[1;94m████████╗██╗░██████╗░███████╗██████╗░
\033[1;94m╚══██╔══╝██║██╔════╝░██╔════╝██╔══██╗
\033[1;97m░░░██║░░░██║██║░░██╗░█████╗░░██████╔╝
\033[1;97m░░░██║░░░██║██║░░╚██╗██╔══╝░░██╔══██╗
\033[1;96m░░░██║░░░██║╚██████╔╝███████╗██║░░██║
\033[1;96m░░░╚═╝░░░╚═╝░╚═════╝░╚══════╝╚═╝░░╚═╝
 
\033[1;97m•◄►•═ ═ ═ ═ ═ ═ ═•◄►•\033[1;92mBangladesh Hacker\033[1;97m•◄►•═ ═ ═ ═ ═ ═ ═•◄►•"""
print  "\033[1;90m🔀 ⚌⚌⚌⚌⚌⚌⚍⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌⚌ 🔀"
jalan("\033[0;31m▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇▶🌷") 
jalan("\033[0;31m▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇▶🌷") 
jalan("\033[0;31m▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇▶🌷") 
jalan("\033[0;31m▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇▶🌷") 
jalan("\033[0;31m▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇▶🌷 ") 
jalan("\033[0;31m▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇▶🌷") 
jalan("\033[1;35m☠ Welcome to Sohag Tech ☠ ") 
jalan("\033[0;37m▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇▶🌷") 
jalan("\033[0;37m▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇▶🌷 ") 
jalan("\033[0;37m▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇▶🌷") 
jalan("\033[0;37m▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇▶🌷") 
jalan("\033[0;37m▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇▶🌷") 
jalan("\033[0;37m▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇ ▇▶🌷") 
print "\033[1;97m•◄►•═ ═ ═ ═ ═ ═ ═•◄►•\033[1;92mBangladesh Hacker\033[1;97m•◄►•═ ═ ═ ═ ═ ═ ═•◄►•"

CorrectUsername = "Sohag"
CorrectPassword = "Sohag"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;97m📋 \x1b[1;93mTool Username \x1b[1;97m»» \x1b[1;97m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;97m🗝 \x1b[1;91mTool Password  \x1b[1;97m»» \x1b[1;97m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Dev:Rana
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;94mWrong Password"
            os.system('xdg-open command make kortechi
