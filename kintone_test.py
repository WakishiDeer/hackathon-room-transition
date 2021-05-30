import requests
import json
import itertools

API_TOKEN = "6cy4QWAVJc3PgcuDZBb8Jn7fJP16AiflZ530Weix"
KINTONE_APP=2
KINTONE_ID=5

def get_kintone(api_token,app,id):
    URL=""
    if id:
        URL = "https://yrx1kimhweye.cybozu.com/k/v1/record.json?app={}&id={}".format(app,id)
    else:
        URL = "https://yrx1kimhweye.cybozu.com/k/v1/records.json?app={}".format(app)
    headers = {"X-Cybozu-API-Token": api_token}
    resp = requests.get(URL, headers=headers)
    return resp

def post_kintone(params, api_token,app):
    URL = "https://yrx1kimhweye.cybozu.com/k/v1/record.json?app={}".format(app)
    headers={"X-Cybozu-API-Token": api_token,"Content-Type" : "application/json"}
    resp = requests.post(URL, json=params, headers=headers)
    return resp

def put_kintone(params, api_token,app ,id):
    URL = "https://yrx1kimhweye.cybozu.com/k/v1/record.json?app={}&id={}".format(app,id)
    headers={"X-Cybozu-API-Token": api_token,"Content-Type" : "application/json"}
    resp = requests.put(URL, json=params, headers=headers)
    return resp

def find_id(api_token,app,id,Header):
    RESP=get_kintone(api_token,app,id)
    data = json.loads(RESP.text)
    data=data['records']
    find_list=[]
    find_id_list=[]
    for d in data:
        find_id_list.append(d['$id']["value"])
        find_list.append(d[Header]["value"])
        
    flg = [True if int(f) > 0 else False for f in find_list]
    print(list(itertools.compress(find_id_list, flg)))

if __name__ == "__main__":
    #状態テーブル

    PARAMS = {
  "app": KINTONE_APP,
  "record": {
    "line_id":{
        "value":"AIOKAKJ"
    },
    "status":{
        "value":0
        },
    "counter":{
        "value":0
    }
  }
}

    params={
    "app": KINTONE_APP,
    "id":KINTONE_ID,
    "record": {
        "status":{
            "value":1
            }
        }
    }


    #RESP = post_kintone(PARAMS,API_TOKEN,KINTONE_APP)
    #RESP = get_kintone(API_TOKEN,KINTONE_APP,KINTONE_ID)
    #RESP = get_kintone(API_TOKEN,KINTONE_APP,None)
    RESP = put_kintone(params,API_TOKEN,KINTONE_APP,KINTONE_ID)
    #find_id(API_TOKEN,KINTONE_APP,None,"counter")
    data = json.loads(RESP.text)
    print(data)
