
# IPtool

# Author - Rattashi




print("IP TOOL HOΕGELDΔ°NΔ°Z")


import json
import urllib.request
import webbrowser
import os
try:
    R='\033[91m'
    Y='\033[93m'
    G='\033[92m'
    CY='\033[96m'
    W='\033[97m'
    path=os.path.isfile('/data/data/com.termux/files/usr/bin/bash')
    def start():
        os.system('clear')
        print (CY+"""
             
     Ip-Tool
"""+R+""""""+Y+"""----"""+CY+"""''ππ’π―πΆπ―πΆπ― ππͺπ¨π¦π³ ππ’π³π’π§πͺπ―π₯π’ π π¦π³ ππ­π΄π’πΊπ₯πͺπ¬, ππ― ππΊπͺ ππΆπ€π­πΆπ­π’π³ ππͺπ» ππ­πΆπ³π₯πΆπ¬.''"""+Y+"""----"""+R+"""""")
        
    def m3():
        try:
            print(R+"""\n
               """+R+"""ββββββββββββββββββββββββββββββββββββββββββββββββββ
               """+R+"""ββββββββββββββββββββββββββββββββββββββββββββββββββ
               """+R+"""ββββββββββββββββββββββββββββββββββββββββββββββββββ
               """+R+"""ββββββββββββββββββββββββββββββββββββββββββββββββββ
               """+R+"""ββββββββββββββββββββββββββββββββββββββββββββββββββ
               """+R+"""ββββββββββββββββββββββββββββββββββββββββββββββββββ
                       """+W+"""βGeliΕtirci: @Rattashi
                       """+W+"""βVersiyon: 1.23
                       """+W+"""βDil: Python
	"""+W+"""β­βββββββββββββββ΄Tarih: 01.12.2022
        """+Y+"""β SeΓ§enekler"""+G+""" >>"""+Y+"""
        """+W+"""β 1-) Kendinizi TarayΔ±n"""+Y+"""
        """+W+"""β 2-) Website TarayΔ±n Γrnek: google.com"""+Y+"""
        """+W+"""β 3-) Ip TarayΔ±n"""+Y+"""
        """+W+"""β 4-) ΓΔ±kΔ±Ε
""")
            ch=int(input(CY+"SeΓ§eneΔi Girdiniz: "+W))
            if ch==1:
                main2()
                m3()
            elif ch==2:
                main()
                m3()
            elif ch==3:
                main()
                m3()
            elif ch==4:
                print(Y+"ΓΔ±kΔ±Ε................"+W)
            else:
                print(R+"\nGeΓ§ersiz!\n")
                m3()
        except ValueError:
            print(R+"\nGeΓ§ersiz!\n")
            m3()
        
    def finder(u):
        try:
            try:
                response = urllib.request.urlopen(u)
                data = json.load(response)

                print(R+"\nβ β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β ")
                print(Y+'\n>>>'+CY+' IP bilgileri\n ')
                print(G+"Durum : "+Y,data['status'],'\n')
                print(G+"1) IP ADRESΔ° : "+Y,data['query'],'\n')
                print(G+"2) Hat : "+Y,data['org'],'\n')
                print(G+"3) Εehir : "+Y,data['regionName'],'\n')
                print(G+"4) Εehir Kodu : "+Y,data['region'],'\n')
                print(G+"5) Δ°lΓ§e : "+Y,data['city'],'\n')
                print(G+"6) Mahalle Kodu : "+Y,data['zip'],'\n')
                print(G+"7) Γlke : "+Y,data['country'],'\n')
                print(G+"8) Yer\n")
                print(G+"\tEnlem : "+Y,data['lat'],'\n')
                print(G+"\tBoylam : "+Y,data['lon'],'\n')
                l='https://www.google.com/maps/place/'+str(data['lat'])+'+'+str(data['lon'])
                print(R+"\n#"+Y+" Google Map AΓ§Δ±lΔ±Ε : "+CY,l)
                path=os.path.isfile('/data/data/com.termux/files/usr/bin/bash')
                if path:
                    link='am start -a android.intent.action.VIEW -d '+str(l)
                    pr=input(R+"\n>>"+Y+" BaΔlantΔ±ya Gitmek Δ°stermisiniz?"+G+" (y|n): "+W)
                    if pr=="y":
                        lnk=str(link)+" > /dev/null"
                        os.system(str(lnk))
                        start()
                        m3()
                    elif pr=="n":
                        print("\nBaΕka Bir IP Bulun Yada ΓΔ±kΔ±n Ctrl + C\n\n")
                        start()
                        m3()
                    else:
                        print("\nTekrar Deneyiniz!\n")
                        m3()
                else:
                    pr=input(R+"\n>>"+Y+" BaΔlantΔ±ya Gitmek Δ°stermisiniz?"+G+" (y|n): "+W)
                    if pr=="y":
                        webbrowser.open(l,new=0)
                        start()
                        m3()
                    elif pr=="n":
                        print(R+"\nβ β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β β ")
                        print(Y+"\nBaΕka Bir IP Bulun Yada ΓΔ±kΔ±n "+R+"Ctrl + C\n\n")
                        start()
                        m3()
                    else:
                        print(R+"\nGeΓ§ersiz!\n")
                        m3()
                return
            except KeyError:
                print(R+"\nHata! Web Sitesi GeΓ§ersiz\n"+W)
                m3()
        except urllib.error.URLError:
            print(R+"\nHata!"+Y+" Δ°nternet BaΔlantΔ±nΔ±zΔ± Kontrol Edin!\n"+W)
            exit()

        
    def main():
        u=input(G+"\n>>> "+Y+"WEB SΔ°TESΔ°NΔ°N ADRESΔ°NΔ° GΔ°RΔ°N:"+W+" ")
        if u=="":
            print(R+"\nWEB SΔ°TESΔ°NΔ°N ADRESΔ°NΔ° GΔ°RΔ°N!")
            main()
        else:
            url ='http://ip-api.com/json/'+u
            finder(url)
    def main2():
        url ='http://ip-api.com/json/'
        finder(url)
        
    def main():
        u=input(G+"\n>>> "+Y+"Ip adresi girin.:"+W+" ")
        if u=="":
            print(R+"\nIp Adresi girin.")
            main()
        else:
            url ='http://ip-api.com/json/'+u
            finder(url)
    def main2():
        url ='http://ip-api.com/json/'
        finder(url)
        
        
    start()
    m3()
except KeyboardInterrupt:
    print(Y+"\nΔ°YΔ° GΓNLER"+W)
