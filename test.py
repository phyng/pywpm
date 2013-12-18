#coding = utf-8
import json
import requests

url = 'https://raw.github.com/phyng/pywpm/master/app/qq.app'
r = requests.get(url)
print (r.json())