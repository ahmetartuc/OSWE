# OSWE Prep Lab List

The following labs will be used to prepare for the **OSWE (Offensive Security Web Expert)** exam.  
Each lab covers different scenarios, vulnerabilities and hands-on testing opportunities.

---

## 1. [Order](https://github.com/bmdyy/order)
- **Focus:** SQLi, Auth Bypass, IDOR  
- **Key Learnings:**  
  - Manual SQL Injection exploitation  
  - Authentication bypass techniques  
  - Insecure Direct Object Reference exploitation  

---

## 2. [Chat.js](https://github.com/bmdyy/chat.js)
- **Focus:** XSS, WebSocket, Auth Flaws  
- **Key Learnings:**  
  - Crafting XSS payloads & filter bypass  
  - Identifying WebSocket vulnerabilities  
  - Authentication flaws in Node.js apps  

---

## 3. [Tudo](https://github.com/bmdyy/tudo)
- **Focus:** Auth Bypass, IDOR, Input Validation  
- **Key Learnings:**  
  - Testing session management in CRUD apps  
  - Manipulating data via IDOR  
  - Exploiting poor input validation  

---

## 4. [Testr](https://github.com/bmdyy/testr)
- **Focus:** File Upload, Command Injection, RCE  
- **Key Learnings:**  
  - Insecure file upload scenarios  
  - Achieving RCE via command injection  
  - File handling security flaws  

---

## 5. [White Box Pentesting](https://github.com/TROUBLE-1/White-box-pentesting)
- **Focus:** SQLi, RCE, LFI/RFI  
- **Key Learnings:**  
  - Source code review for vulnerability discovery  
  - White-box exploitation (OSWE-style practice)  
  - Local/Remote File Inclusion attack chains  

---

## 6. [Web Hacking Playground](https://github.com/takito1812/web-hacking-playground)
- **Focus:** XSS, CSRF, SQLi, File Upload, SSRF  
- **Key Learnings:**  
  - Broad vulnerability coverage  
  - CSRF token manipulation  
  - SSRF → internal service discovery  

---

## 7. [SecureCode: 1](https://www.vulnhub.com/entry/securecode-1,651/)
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

## 8. [Potato: 1](https://www.vulnhub.com/entry/potato-1,529/)
- **Type:** Boot2Root (Web + SSH)  
- **Difficulty:** Easy–Medium  
- **Flags:** `user.txt` and `root.txt`  
- **Key Learnings:**  
  - Full port & service enumeration  
  - Directory/file discovery (dirbusting)  
  - PHP code review (possible type juggling)  
  - SSH access + privilege escalation (sudo misconfig, etc.)  

---

## 9. [Raven: 1](https://www.vulnhub.com/entry/raven-1,256/)
- **Type:** Boot2Root (Web app + system exploitation)  
- **Difficulty:** Beginner–Intermediate  
- **Flags:** Total of 4 flags, with at least 2 root paths  
- **Key Learnings:**  
  - WordPress/CMS enumeration & vulnerability scanning  
  - Hidden directory/file discovery  
  - SSH access → multiple privilege escalation paths
