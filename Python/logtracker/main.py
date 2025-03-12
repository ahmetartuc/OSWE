import re
import json
import xml.etree.ElementTree as ET
import requests
import logging

logging.basicConfig(filename="analysis_log.txt", level=logging.INFO, format="%(asctime)s - %(levelname)s: %(message)s")

def read_log(file_name):
    try:
        with open(file_name, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        logging.error("Error: Log file not found!")
        return []

def analyze_log(logs):
    ip_pattern = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"
    error_codes = ["403", "500", "401"]

    analysis_result = []

    for line in logs:
        ip_address = re.search(ip_pattern, line)
        error_code = re.search(r"\s(403|500|401)\s", line)

        if ip_address and error_code:
            analysis_result.append({"ip": ip_address.group(), "error_code": error_code.group().strip()})

    return analysis_result

def query_ip(ip_address):
    try:
        response = requests.get(f"https://ipapi.co/{ip_address}/json/")
        if response.status_code == 200:
            return response.json().get("country_name", "Unknown")
        else:
            return "Unknown"
    except requests.exceptions.RequestException:
        logging.error(f"Error: Could not retrieve IP information for {ip_address}.")
        return "Unknown"

def save_json(data, file_name="report.json"):
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)
    print(f"Report saved as JSON in {file_name}.")

def save_xml(data, file_name="report.xml"):
    root = ET.Element("log_analysis")

    for item in data:
        entry = ET.SubElement(root, "entry")
        ET.SubElement(entry, "ip").text = item["ip"]
        ET.SubElement(entry, "error_code").text = item["error_code"]
        ET.SubElement(entry, "country").text = item.get("country", "Unknown")

    tree = ET.ElementTree(root)
    tree.write(file_name, encoding="utf-8", xml_declaration=True)
    print(f"Report saved as XML in {file_name}.")

def main():
    logs = read_log("server.log")
    if not logs:
        print("Log file not found.")
        return

    analysis_result = analyze_log(logs)

    for entry in analysis_result:
        entry["country"] = query_ip(entry["ip"])

    save_json(analysis_result)
    save_xml(analysis_result)

    print("Log analysis completed!")

if __name__ == "__main__":
    main()
