
# รายชื่อ บลจ.

import http.client
import urllib.request
import urllib.parse
import urllib.error
import base64
import json
import pandas as pd

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': "9a59e81ff953449e9df599624eed1968",
}

params = urllib.parse.urlencode({
})

try:
    conn = http.client.HTTPSConnection('api.sec.or.th')
    conn.request("GET", "/FundFactsheet/fund/M0432_2560/policy?%s" % params, "{body}", headers)
    data = pd.read_json(conn.getresponse())
    #response = conn.getresponse()
    #data =  response.read()    
    print(data)
   
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
   
f = open('company.txt','w',encoding='utf-8')
f.write (str(data))
#หรือ f.writelines(s)
f.close()



########### Python 3.2 #############
