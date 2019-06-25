import urllib.request
import urllib.parse
import json
import time
while True:

    content = input('请输入想要翻译的内容(输入quit退出程序):')
    if content == 'quit':
        break
    url= 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'

    data = {}
    data['i']=content
    data['from']='AUTO'
    data['to']='AUTO'
    data['smartresult']='dict'
    data['client']='fanyideskweb'
    data['salt']='15614303838964'
    data['sign']='eca62d5f6dfeb9d261972bb9a76e9e91'
    data['ts']='1561430383896'
    data['bv']='a973a95daa8518a82e41685ce156ae19'
    data['doctype']='json'
    data['version']='2.1'
    data['keyfrom']='fanyi.web'
    data['action']='FY_BY_CLICKBUTTION'
    data = urllib.parse.urlencode(data).encode('utf-8')
    '''
    req = urllib.request.Request(url,data)
    req = add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36')
    '''
    req = urllib.request.Request(url,data,head)
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')

    target = json.loads(html)
    target = target['translateResult'][0][0]['tgt']

    print(target)
    time.sleep(5)