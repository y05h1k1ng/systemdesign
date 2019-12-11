import requests
import json

url = "http://localhost:9999"
header = {"content-type": "application/json"}

def main():
    payload = {"city": "hoge"}
    r = requests.post(url+"/api", data=json.dumps(payload), headers=header)
    res = r.json()
    print("[+] response json:", res)
    if res["Level"] >= 7:
        print(" [+] warning!")

if __name__=="__main__":
    main()
