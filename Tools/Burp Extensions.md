# Burp Suite Extensions

Extensions that convert HTTP requests from Burp Suite into source code in various programming languages. Useful for scripting, PoC development, and automation.

---

## Copy As Python-Requests

**Extension URL:** [https://portswigger.net/bappstore/b324647b6efa4b6a8f346389730df160](https://portswigger.net/bappstore/b324647b6efa4b6a8f346389730df160)  
**Source:** [https://github.com/portswigger/copy-as-python-requests](https://github.com/portswigger/copy-as-python-requests)

### Usage
1. In Burp: Go to **Extender > BApp Store**, and install the “HTTP Request to Python Requests” extension.
2. Right-click on a request → Select **"Copy as Python requests"**.

### Notes
- Cookie management must be handled manually.
- For bodies containing `multipart/form-data`, manual editing may be required.

---

## Copy As Go Request

**Extension URL:** [https://portswigger.net/bappstore/b2f4605661f249a5a5b452ee63d5aa77](https://portswigger.net/bappstore/b2f4605661f249a5a5b452ee63d5aa77)  
**Source:** [https://github.com/portswigger/copy-as-go-request](https://github.com/portswigger/copy-as-go-request)

### Usage
1. Right-click a request to invoke the context menu.
2. Select **Extensions > Copy as Go request**.
3. Choose raw or base64-encoded version.

---

## Copy as Node Request

**Extension URL:** [https://portswigger.net/bappstore/3eaf7d7a8f0d48ef84f9c8bc6166c89e](https://portswigger.net/bappstore/3eaf7d7a8f0d48ef84f9c8bc6166c89e)  
**Source:** [https://github.com/portswigger/copy-as-node-request](https://github.com/portswigger/copy-as-node-request)

---

## Copy As PowerShell Requests

**Extension URL:** [https://portswigger.net/bappstore/27b204297a5b4cd1912df2f25f3c1e61](https://portswigger.net/bappstore/27b204297a5b4cd1912df2f25f3c1e61)  
**Source:** [https://github.com/portswigger/copy-as-powershell-requests](https://github.com/portswigger/copy-as-powershell-requests)

---

## Copy as Python httpx

**Extension URL:** [https://portswigger.net/bappstore/99691b688a86482fa6fc262108dfaee4](https://portswigger.net/bappstore/99691b688a86482fa6fc262108dfaee4)  
**Source:** [https://github.com/portswigger/copy-as-python-httpx](https://github.com/portswigger/copy-as-python-httpx)

### Features
- Export HTTP/1.1 and HTTP/2 requests.
- Uses `httpx` for Python scripts.

### Usage
1. Right-click a request and use the extension-generated context menu item.
2. The converted request will be stored in your clipboard.

---

## Copy as Python aiohttp

**Extension URL:** [https://portswigger.net/bappstore/1c2c2b9b55df4e12954b4e2d1a72b071](https://portswigger.net/bappstore/1c2c2b9b55df4e12954b4e2d1a72b071)  
**Source:** [https://github.com/portswigger/copy-as-python-aiohttp](https://github.com/portswigger/copy-as-python-aiohttp)

### Features
- Generates async Python code from HTTP requests.
- Supports:
  - individual async functions
  - session handling
  - password spraying automation

---

