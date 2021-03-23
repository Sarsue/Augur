import json
import smtplib
import os
from dotenv import load_dotenv


load_dotenv()

# https://support.gomotionapp.com/en/articles/407-email-to-sms-gateway-list

carriers = {
    "att": "@mms.att.net",
    "tmobile": " @tmomail.net",
    "verizon": "@vtext.com",
    "sprint": "@page.nextel.com",
    "freedom": "@txt.freedommobile.ca",
    "virgin": "@vmobile.ca",
    "rogers": "@pcs.rogers.com",
}
 # move to config or get from file system
recipients = {
        "5147798178": "virgin",
        "6136143467": "freedom",
        "4379285776": "rogers",
    }

def send_txt(message):
    # Replace the number with your own, or consider using an argument\dict for multiple people.
    for key in recipients:
        to_number = f"{key}{carriers[recipients[key]]}"
        auth = (
            os.environ.get("APP_NOTIFICATION_EMAIL"),
            os.environ.get("APP_NOTIFICATION_PASSWORD"),
        )
        # Establish a secure session with gmail's outgoing SMTP server using your gmail account
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(auth[0], auth[1])

        # Send text message through SMS gateway of destination number
        server.sendmail(auth[0], to_number, message)


def send_email(to, subject, message):
    pass


if __name__ == "__main__":
    # send_txt(msg)
