import requests
import json

url = "http://localhost:8888"
header = {"content-type": "application/json"}

def main():
    r = requests.get(url+"/tsunami", headers=header)
    res = r.json()
    print("[+] tsunami response:", res)
    r = requests.get(url+"/rain", headers=header)
    res = r.json()
    print("[+] rain response:", res)
    r = requests.get(url+"/earthquake", headers=header)
    res = r.json()
    print("[+] earthquake response:", res)
    r = requests.get(url+"/volcano", headers=header)
    res = r.json()
    print("[+] volcano response:", res)
    

if __name__=="__main__":
    main()
