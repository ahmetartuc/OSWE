#!/usr/bin/env python3
from datetime import datetime
from secure_smtpd import SMTPServer, FakeCredentialValidator
from smtplib import SMTP_SSL as SMTP
import asyncore, logging, sys, os

SMTPserver = 'mail.oswe.com'
USERNAME = "null"
PASSWORD = "hex"

def send_message(peer, mailfrom, rcpttos, data):
    try:
        conn = SMTP(SMTPserver, port=465)
        conn.login(USERNAME, PASSWORD)
        try:
            conn.sendmail(mailfrom, rcpttos, data)
        finally:
            conn.quit()
    except Exception as exc:
        sys.exit("Mail failed: %s" % str(exc))

class SMTPForwarder(SMTPServer):
    def __init__(self):
        pass

    def start(self):
        SMTPServer.__init__(
            self,
            ('0.0.0.0', 25),
            None,
            require_authentication=True,
            credential_validator=FakeCredentialValidator(),
            process_count=1
        )
        print("[*] SMTP Forwarder running on port 25...")
        asyncore.loop()

    def process_message(self, peer, mailfrom, rcpttos, data):
        print(f"[+] Mail received from {mailfrom}, forwarding...")
        send_message(peer, mailfrom, rcpttos, data)

def run():
    server = SMTPForwarder()
    server.start()

if __name__ == '__main__':
    run()
