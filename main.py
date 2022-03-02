import requests
from bs4 import BeautifulSoup
import socket
from urllib.request import Request, urlopen
import time

import random
import string
import sys
import threading


def generate_random_string(length):
    letters_and_digits = string.ascii_lowercase + string.digits
    rand_string = ''.join(random.sample(letters_and_digits, length))
    #print("Alphanum Random string of length", length, "is:", rand_string)
    return rand_string

def request():
    count = 0
    for j in range(5,7+1,1):
        for i in range(0,1000,1):
            url0 = 'http://prnt.sc/'+generate_random_string(j)
            time.sleep(1)
            res = requests.get(url0, headers={'User-Agent': 'Chrome'+generate_random_string(2)})
            if(res):
                soup = BeautifulSoup(res.text, 'lxml')
                if(soup.find('img', class_='no-click screenshot-image')):
                    src = soup.find('img', class_='no-click screenshot-image').get('src')
                    image_id = soup.find('img', class_='no-click screenshot-image').get('image-id')
                    if(not (src[2: 16]=='st.prntscr.com')):
                        """
                        response = requests.get(src, stream=True)
                        out = open("img/img_"+image_id+".png",'wb')
                        out.write(response.content)
                        out.close()
                        """
                        time.sleep(1)
                        try:
                            req = Request(src,headers={'User-Agent': 'Chrome'+generate_random_string(2)})
                            webpage = urlopen(req)
                            if(webpage):
                                count += 1
                                print('OK '+str(count))
                                content = webpage.read()
                                out = open("img/img_"+image_id+".png", "wb")
                                out.write(content)
                                out.close
                            else:
                                count += 1
                                print('Failed '+str(count))
                        except:
                            count += 1
                            print('Failed '+str(count))
                    else:
                        count += 1
                        print('Failed '+str(count))
                else:
                    count += 1
                    print('Failed '+str(count))
            else:
                count += 1
                print('Failed '+str(count))

if __name__ == '__main__':
    #sys.setrecursionlimit(1000000)
    request()
    """
    t0 = threading.Thread(target=request)
    t1 = threading.Thread(target=request)
    t2 = threading.Thread(target=request)
    t3 = threading.Thread(target=request)
    t4 = threading.Thread(target=request)
    t5 = threading.Thread(target=request)
    t6 = threading.Thread(target=request)
    t7 = threading.Thread(target=request)
    t8 = threading.Thread(target=request)
    t9 = threading.Thread(target=request)

    t0.start()
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()

    t0.join()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()
    t9.join()
    """