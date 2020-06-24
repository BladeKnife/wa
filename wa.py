import os,sys,requests,json,re,time,random
from requests import post
from time import sleep
def rupa():
    ua={
    "Host": "wapi.ruparupa.com",
    "Connection": "keep-alive",
    "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiOGZlY2VjZmYtZTQ1Zi00MTVmLWI2M2UtMmJiMzUyZmQ2NzhkIiwiaWF0IjoxNTkzMDIyNDkyLCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.fETKXQ0KyZdksWWsjkRpjiKLrJtZWmtogKyePycoF0E",
    "Accept": "application/json",
    "Content-Type": "application/json",
    "X-Company-Name": "odi",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
    "user-platform": "mobile",
    "X-Frontend-Type": "mobile",
    "Origin": "https://m.ruparupa.com",
    "Referer": "https://m.ruparupa.com/verification?page=otp-choices",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    dat=json.dumps({"phone":no,"action":"register","channel":"chat","email":"","customer_id":"0","is_resend":0})
    r = requests.post("https://wapi.ruparupa.com/auth/generate-otp", data=dat, headers=ua).text
    if "success" in r:
        print ("\033[1;97mSPAM \033[90m=> \033[1;92mBERHASIL")
    else:
        print ("\033[1;97mSPAM \033[90m=> \033[1;91mGAGAL")
        sys.exit("\033[1;97mLimit Gan")
def tok():
    ua = {
    'Connection' : 'keep-alive',
    'Accept' : 'application/json, text/javascript, */*; q=0.01',
    'Origin' : 'https://accounts.tokopedia.com',
    'X-Requested-With' : 'XMLHttpRequest',
    'User-Agent' : 'Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36',
    'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept-Encoding' : 'gzip, deflate',
    }
    site = requests.get('https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn='+no+'&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D',headers=ua).text
    search = re.search(r'\<input\ id\=\"Token\"\ value\=\"(.*?)\"\ type\=\"hidden\"\>', site).group(1)
    data = {
    'otp_type' : '116',
    'msisdn' : no,
    'tk' : search,
    'email' : '',
    'original_param' : '',
    'user_id' : '',
    'signature' : '',
    'number_otp_digit' : '6',
    }
    send = requests.post('https://accounts.tokopedia.com/otp/c/ajax/request-wa', headers=ua, data=data).text
    if "true" in send:
        print ("\033[1;97mSPAM \033[90m=> \033[1;92mBERHASIL")
    else:
        print ("\033[1;97mSPAM \033[90m=> \033[1;91mGAGAL")
        sys.exit("\033[1;97mLimit Gan")
#koid
def red():
    agent = requests.get('https://pastebin.com/raw/zkCXTGcm').text.split('\n')
    acak = random.choice(agent)
    ua={
    "Host": "m.redbus.id",
    "accept": "application/json, text/plain, */*",
    "user-agent": acak,
    "referer": "https://m.redbus.id/",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
    "cookie": "G_ENABLED_IDPS=google",
    "cookie": "country=IDN",
    "cookie": "language=id",
    }
    r = requests.get("https://m.redbus.id/api/getOtp?number="+no+"&cc=62&whatsAppOpted=true", headers=ua).text
    if "OTP Sent Successfully" in r:
        print ("\033[1;97mSPAM \033[90m=> \033[1;92mSUCCESS")
    else:
        print ("\033[1;97mSPAM \033[90m=> \033[1;91mGAGAL")
        sys.exit("\033[1;97mLimit Gan")
os.system("clear")
print ("""
\033[1;97mSPAM WA
\033[1;97mCreator:\033[1;96mFahmiApz
\033[1;97mYoutube:\033[1;92mKnifer12
\033[90m------------------------------""")
no = input("\033[1;97mNo Target: \033[1;92m")
for i in range(1,3):
    tok()
for i in range(1,3):
    rupa()
    sleep(300)
