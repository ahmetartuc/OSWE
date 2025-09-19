# OSWE Prep Lab List

The following labs will be used to prep for the **OSWE (Offensive Security Web Expert)** exam.  

---

## GitHub Labs

### 1. [Order](https://github.com/bmdyy/order)
- **Focus:** SQLi, Auth Bypass, IDOR  
- **Key Learnings:**  
  - Manual SQL Injection exploitation  
  - Authentication bypass techniques  
  - Insecure Direct Object Reference exploitation  

---

### 2. [Chat.js](https://github.com/bmdyy/chat.js)
- **Focus:** XSS, WebSocket, Auth Flaws  
- **Key Learnings:**  
  - Crafting XSS payloads & filter bypass  
  - Identifying WebSocket vulnerabilities  
  - Authentication flaws in Node.js apps  

---

### 3. [Tudo](https://github.com/bmdyy/tudo)
- **Focus:** Auth Bypass, IDOR, Input Validation  
- **Key Learnings:**  
  - Testing session management in CRUD apps  
  - Manipulating data via IDOR  
  - Exploiting poor input validation  

---

### 4. [Testr](https://github.com/bmdyy/testr)
- **Focus:** File Upload, Command Injection, RCE  
- **Key Learnings:**  
  - Insecure file upload scenarios  
  - Achieving RCE via command injection  
  - File handling security flaws  

---

### 5. [White Box Pentesting](https://github.com/TROUBLE-1/White-box-pentesting)
- **Focus:** SQLi, RCE, LFI/RFI  
- **Key Learnings:**  
  - Source code review for vulnerability discovery  
  - White-box exploitation (OSWE-style practice)  
  - Local/Remote File Inclusion attack chains  

---

### 6. [Web Hacking Playground](https://github.com/takito1812/web-hacking-playground)
- **Focus:** XSS, CSRF, SQLi, File Upload, SSRF  
- **Key Learnings:**  
  - Broad vulnerability coverage  
  - CSRF token manipulation  
  - SSRF → internal service discovery  

---

## VulnHub Labs

### 7. [SecureCode: 1](https://www.vulnhub.com/entry/securecode-1,651/)
- **Type:** OSWE-like machine (Linux + PHP web app)  
- **Difficulty:** Easy–Medium  
- **Flags:**  
  1. Authentication bypass → flag1  
  2. Remote Command Execution (RCE) → flag2  
- **Key Learnings:**  
  - Source code review for vulnerability detection  
  - SQL Injection exploitation  
  - Insecure file upload → shell execution  
  - Chaining auth bypass → RCE  

---

### 8. [Potato: 1](https://www.vulnhub.com/entry/potato-1,529/)
- **Type:** Boot2Root (Web + SSH)  
- **Difficulty:** Easy–Medium  
- **Flags:** `user.txt` and `root.txt`  
- **Key Learnings:**  
  - Full port & service enumeration  
  - Directory/file discovery (dirbusting)  
  - PHP code review (possible type juggling)  
  - SSH access + privilege escalation (sudo misconfig, etc.)  

---

### 9. [Raven: 1](https://www.vulnhub.com/entry/raven-1,256/)
- **Type:** Boot2Root (Web app + system exploitation)  
- **Difficulty:** Beginner–Intermediate  
- **Flags:** Total of 4 flags, with at least 2 root paths  
- **Key Learnings:**  
  - WordPress/CMS enumeration & vulnerability scanning  
  - Hidden directory/file discovery  
  - SSH access → multiple privilege escalation paths  

---

### 10. [Silky-CTF: 0x02](https://www.vulnhub.com/entry/silky-ctf-0x02,307/)
- **Type:** Boot2Root CTF-style  
- **Difficulty:** Medium  
- **Key Learnings:**  
  - Multiple chained vulnerabilities (web + system)  
  - Web app enumeration and exploitation  
  - Privilege escalation through misconfigurations  

---

### 11. [bWAPP](https://www.vulnhub.com/series/bwapp,34/)
- **Type:** Intentionally Vulnerable Web App  
- **Difficulty:** Beginner–Advanced (wide range)  
- **Key Learnings:**  
  - Huge variety of web vulnerabilities (XSS, SQLi, CSRF, etc.)  
  - Good practice for payload crafting & testing  
  - Ideal for building exploit scripts  

---

### 12. [Homeless 1](https://www.vulnhub.com/entry/homeless-1,215/)
- **Type:** Boot2Root (Linux)  
- **Difficulty:** Beginner–Intermediate  
- **Key Learnings:**  
  - Web exploitation + privilege escalation  
  - Basic enumeration techniques  
  - Good for OSCP/OSWE warm-up  

---

### 13. [Seattle 0.3](https://www.vulnhub.com/entry/seattle-v03,145/)
- **Type:** Boot2Root (Linux)  
- **Difficulty:** Intermediate  
- **Key Learnings:**  
  - Web application vulnerabilities → system compromise  
  - Practicing local privilege escalation  
  - Custom web app analysis  

---

### 14. [Ted 1](https://www.vulnhub.com/entry/ted-1,327/)
- **Type:** Boot2Root (Linux)  
- **Difficulty:** Intermediate  
- **Key Learnings:**  
  - Source code review challenges  
  - SQLi and file inclusion exploitation  
  - Pivoting from web to root  

---

### 15. [Raven 2](https://www.vulnhub.com/entry/raven-2,269/)
- **Type:** Boot2Root (Linux, WordPress-based)  
- **Difficulty:** Beginner–Intermediate  
- **Key Learnings:**  
  - CMS (WordPress) enumeration and exploitation  
  - Database extraction & password reuse  
  - Privilege escalation to root  

---

### 16. [Pipe](https://www.vulnhub.com/entry/devrandom-pipe,124/)
- **Type:** Boot2Root (Linux)  
- **Difficulty:** Intermediate–Hard  
- **Key Learnings:**  
  - Chained exploitation of multiple vulnerabilities  
  - Reverse engineering and custom script analysis  
  - Privilege escalation via kernel/system misconfigs  

---

### 17. [Flick 2](https://www.vulnhub.com/entry/flick-2,122/)
- **Type:** Boot2Root (Linux, Web App)  
- **Difficulty:** Hard  
- **Key Learnings:**  
  - Advanced web exploitation scenarios  
  - Source code review and manual exploit crafting  
  - Realistic OSWE-style exploitation path  
