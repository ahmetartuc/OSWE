# Web Log Analysis & Reporting Tool  

## 📌 What’s This About?
This python script **scans server logs**, **hunts down error messages**, **extracts IP addresses** then **fetches extra data from an API** and finally **spits out a clean JSON and XML report** just for you!  

## 📌 What’s Under the Hood? (Libraries in Action)
+ **`re` (Regex - Data Sniper)**  
+ **`requests` (Yeah, we pull data from APIs, so what?)**  
+ **`json` (To store everything neat and clean)**  
+ **`xml.etree.ElementTree` (For XML junkies)**  
+ **`logging` (Because we need to remember our mistakes)**

---

## Output
## report.json
```json
[
    {
        "ip": "172.16.0.5",
        "error_code": "403",
        "country": "Unknown"
    },
    {
        "ip": "10.0.0.25",
        "error_code": "500",
        "country": "Unknown"
    },
    {
        "ip": "192.168.1.15",
        "error_code": "401",
        "country": "Unknown"
    }
]
```
## report.xml
```xml
report.xml    
<?xml version='1.0' encoding='utf-8'?>
<log_analysis><entry><ip>172.16.0.5</ip><error_code>403</error_code><country>Unknown</country></entry><entry><ip>10.0.0.25</ip><error_code>500</error_code><country>Unknown</country></entry><entry><ip>192.168.1.15</ip><error_code>401</error_code><country>Unknown</country></entry></log_analysis>                                        
```
