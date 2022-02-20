import os, requests
'''
✔️ input()
✔️ split()
✔️ strip()
✔️ lower()
✔️ join()
✔️ requests.get()
✔️ for item in items :
✔️ try: except:
✔️ while, break
'''
while (True):
    urls=input("# Please write a URL or URLs you want to check. (separated by commas)\n>>>")
    parsed= urls.split(',')
    for url in parsed:
        url=url.strip().lower()
        if 'http://' not in url:
            url=''.join(('http://',url))
        try:
            r=requests.get(url)
            result="up!"
        except:
            result="down!"
        print(url,'is',result)
    reply=input("Do you want to start over? [y/n]")
    if reply=='n':
        break