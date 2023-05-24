#!/bin/env/python3

# Stanley L. Ferguson III
# 23May2023

import logging
import datetime
import ping3
import time
import socket
import smtplib
import os
from logging.handlers import RotatingFileHandler

# Configure logging settings
log_file = 'app.log'
max_log_size = 1024 * 1024  # 1 MB
max_log_files = 5

log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
log_handler = RotatingFileHandler(log_file, maxBytes=max_log_size, backupCount=max_log_files)
log_handler.setFormatter(log_formatter)
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(log_handler)

# Function to send email notification
def send_notification(from_address, to_address, password, subject, body):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_address, password)
        message = 'Subject: {}\n\n{}'.format(subject, body)
        server.sendmail(from_address, to_address, message)
        logging.info("Notification sent successfully")
    except Exception as e:
        logging.error("Notification could not be sent. Error: %s", str(e))
    finally:
        server.quit()

# Ask for user's email address and password
from_address = input("Enter your email address: ")
password = input("Enter your password: ")

# Set the email recipient address
to_address = "Jeremypatton6@gmail.com"

# Set the initial host status
host_status = False

while True:
    # Ping the host to check its status
    hostname = "example.com"  # Replace with the host you want to ping
    response = os.system("ping -n 1 " + hostname)
    
    # Check if the host status has changed
    if response == 0 and not host_status:
        subject = "Host status changed"
        body = "{} is now up at {}".format(hostname, datetime.datetime.now())
        host_status = True
        send_notification(from_address, to_address, password, subject, body)
        logging.info("Host status changed to up")
    elif response != 0 and host_status:
        subject = "Host status changed"
        body = "{} is now down at {}".format(hostname, datetime.datetime.now())
        host_status = False
        send_notification(from_address, to_address, password, subject, body)
        logging.warning("Host status changed to down")

    time.sleep(60)  # Wait for 60 seconds before checking again

#this script written with assistance from Google Bard.
