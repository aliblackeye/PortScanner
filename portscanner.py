import socket # Belirtilen ip adresine bağlanmaya ve açık portları bulmaya yarar.
import threading # çoklu çekirdekle işlem yapmak için
import concurrent.futures # çoklu çekirdek kullanırken tüm portları döngüde olarak taramak için gerekli.
import colorama # uygulamayı renklendirir ve güzel gözükmesini sağlar.
from colorama import Fore
colorama.init()


print(Fore.MAGENTA + """
           _ _    _  __                              
     /\   | (_)  | |/ /                              
    /  \  | |_   | ' / __ _ _ __ __ _  __ _  ___ ____
   / /\ \ | | |  |  < / _` | '__/ _` |/ _` |/ _ \_  /
  / ____ \| | |  | . \ (_| | | | (_| | (_| | (_) / / 
 /_/    \_\_|_|  |_|\_\__,_|_|  \__,_|\__, |\___/___|
                                       __/ |         
                                      |___/          
*******************************************************
* https://github.com/aliblackeye
* https://www.linkedin.com/in/ali-karag%C3%B6z-259809225/
""")

print_lock = threading.Lock()

ip = input("Taranacak IP adresi: ")



def PortTarayici(ip,port):
    tarayici = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # parametre olarak ipv4 adresi ve tcp kullanacigimizi belirttik.
    tarayici.settimeout(1) # zaman aşımı 1 sn
    try:
        tarayici.connect((ip,port))
        tarayici.close()
        with print_lock:
            print(Fore.WHITE + f"{port}" + Fore.GREEN + " AÇIK")

    except:
        pass



with concurrent.futures.ThreadPoolExecutor(max_workers=100) as calistirici: 
    for port in range(1000):
        calistirici.submit(PortTarayici, ip, port + 1)