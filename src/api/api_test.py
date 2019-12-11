import requests
import json

url = "http://localhost:9999"
header = {"content-type": "application/json"}

def main():
    payload = {"city": "nara"}
    r = requests.post(url+"/typhoon", data=json.dumps(payload), headers=header)
    res = r.json()
    print("[+] typhoon response:", res)
    r = requests.post(url+"/rain", data=json.dumps(payload), headers=header)
    res = r.json()
    print("[+] rain response:", res)
    r = requests.post(url+"/earthquake", data=json.dumps(payload), headers=header)
    res = r.json()
    print("[+] earthquake response:", res)


if __name__=="__main__":
    main()
