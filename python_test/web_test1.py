#web_test1.py
import urllib

res = urllib.response('www.baidu.com')
print(res.read())