####################################
# Author : ToxicNoob
# GitHub : https://github.com/Toxic-Noob/
# Coder   : HunterSl4d3
# You Have No Permission To Copy Any Codes
# Coping Others Code Will Not Make You a Coder
####################################

import time, sys, os, re
import requests
ses = requests.Session()
urls="https://business.facebook.com/business_locations"

def psb(z):
    for p in z + "\n":
        sys.stdout.write(p)
        sys.stdout.flush()
        time.sleep(0.03)

def save_token(token):
    file = open(".token", "w")
    file.write(token)
    file.close()

###UserAgent###
def user_agent():
            if os.path.exists(".agent"):
                data = open(".agent", "r").read()
            else:
                psb("\033[92m\n    [*] Go To Your Browser, Copy your UserAgent and Past Here For Safe Login...")
                os.system("xdg-open https://google.com/search?q=my+user+agent")
                time.sleep(1)
                data = input("\n    [*] Enter Your User Agent:> \033[37m")
                file = open(".agent", "w")
                file.write(data)
                file.close()
            return data


###Email_Login###
def email_login():
    agent  = user_agent()
    user = input("\033[92m\n    [*] Enter Your Number/Email:> \033[37m")
    pw = input("\033[92m\n    [*] Enter Your Password:> \033[37m")
    while (len(pw) < 6):
        psb("\n\033[91m    [*] Please Check Your Password and Enter Again...")
        pw = input("\033[92m\n    [*] Enter Your Password:> \033[37m")
    time.sleep(0.6)
    try:
        head = {
            'Host' : 'm.facebook.com',
                'cache-control' : 'max-age=0',
            'upgrade-insecure-requests' : '1',
                'user-agent' : agent,
            'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-mode' : 'navigate',
                'sec-fetch-user' : '?1',
            'sec-fetch-dest' : 'document',
                'accept-encoding' : 'gzip, deflate',
            'accept-language' : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
        }
        try:
            r = ses.get("https://m.facebook.com/", headers = head).text.encode('utf-8')
        except:
            r = ses.get("https://m.facebook.com/", headers = head).text
        head2 = {
            'Host' : 'm.facebook.com',
                'user-agent' : agent,
            'content-type' : 'application/x-www-form-urlencoded',
                'x-fb-lsd' : re.search('name="lsd" value="(.*?)"', str(r)).group(1),
            'accept' : '*/*',
                'origin' : 'https://m.facebook.com',
            'sec-fetch-site' : 'same-origin',
                'sec-fetch-mode' : 'cors',
            'sec-fetch-dest' : 'empty',
                'referer' : 'https://m.facebook.com/',
            'accept-encoding' : 'gzip, deflate',
                'accept-language' : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
        }
        payload = {
            "fb_dtsg" : re.search('{"token":"(.*?)"', str(r)).group(1),
                "lsd" : re.search('name="lsd" value="(.*?)"', str(r)).group(1),
            "jazoest" : re.search('name="jazoest" value="(.*?)"', str(r)).group(1),
                "m_ts" : re.search('name="m_ts" value="(.*?)"', str(r)).group(1),
            "li" : re.search('name="li" value="(.*?)"', str(r)).group(1),
                "try_number" : "0",
            "unrecognized_tries" : "0",
                "prefill_contact_point" : user,
            "prefill_source" : "browser_dropdown",
                "prefill_type" : "contact_point",
            "first_prefill_source" : "browser_dropdown",
                "first_prefill_type" : "contact_point",
            "had_cp_prefilled" : True,
                "had_password_prefilled" : False,
            "is_smart_lock" : False,
                "bi_xrwh" : "0",
            "__dyn" : "",
                "__csr" : "",
            "__req" : "2",
                "__a" : "",
            "__user" : "0",
                "email" : user,
            "encpass" : "#PWD_BROWSER:0:"+real_time()+":"+pw
        }
        ses.post("https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100", headers = head2, data = payload)
        cookie = ses.cookies.get_dict()
        if 'c_user' in (cookie):
            head = {
                'Host' : 'business.facebook.com',
                    'cache-control' : 'max-age=0',
                'upgrade-insecure-requests' : '1',
                    'user-agent' : 'Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36',
                'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                    'content-type' : 'text/html; charset=utf-8',
                'accept-encoding' : 'gzip, deflate',
                    'accept-language' : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
            }    
            r = ses.get(urls, headers = head)
            p = re.search('(EAAG\w+)', r.text)
            token = p.group(1)
            save_token()
        elif "checkpoint" in (cookie):
            psb("\n\033[91m    [*] Your ID is In Checkpoint!!\033[37m")
        else:
            psb("\n\033[91m    [*] Your Email or Password is Wrong!!\033[37m")
    except AttributeError:
        psb("\n\033[91m    [*] Your Email or Password is Wrong!!\033[37m")


###Cookie_Login###
def cookie_login():
    cookies = input("\n\033[92m    [*] Enter Your Cookie:> \033[37m")
    time.sleep(0.6)
    try:
        head = {
            'Host' : 'business.facebook.com',
                'cache-control' : 'max-age=0',
            'upgrade-insecure-requests' : '1',
                'user-agent' : 'Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36',
            'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'content-type' : 'text/html; charset=utf-8',
            'accept-encoding' : 'gzip, deflate',
                'accept-language' : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'cookie' : cookies
        }         
        r = ses.get(urls, headers = head)
        p = re.search('(EAAG\w+)', r.text)
        token = p.group(1)
        save_token(token)
    except (AttributeError, requests.exceptions.TooManyRedirects):
        psb("\n\033[91m    [*] Cookie Expired!!\033[37m")


###TokenLogin###
def  token_login():
    token = input("\n\033[92m    [*] Past Your Token:> \033[37m")
    save_token(token)