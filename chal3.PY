#!/usr/bin/env python3

# uptime sensor tool p2
# Stanley L. Ferguson III
# 18 Apr 2023
# create an uptime sensor that uses ICMP packets to determine if a host is up or down


import os, time, smtplib 
from datetime import datetime
from getpass import getpass 

# Assign variables
currentTime = datetime.now()
up = "Up"
down = "Down"


#prompts for email to use for notifications.
email = input("Please enter your email address\n")
pw = getpass("Please enter the password\n")
#asks user for input of ip address
target = input("Please enter an IP address\n")
print("\n")

#  compare previous ping status with current.
def ping_test(target): 
    global last
    ping_result = os.system("ping -c 1 " + target)
        #Check if host is up or down
    if ping_result == 0:
        state = up
        
    elif ping_result != 0:
        state = down
    return state
def send_message(status):

    #create session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    # start TLS for security
    s.starttls()
    # Authenticate
    s.login(email, pw)
    # send an email 
    message = f"Server is {status.lower()}"
    s.sendmail(email,email, message)
    # end session
    s.quit()

last = ping_test(target)

#Infinite loops to keep pinging target with 2 second delay between pings
while True:
    current_state = ping_test(target)
    if current_state != last:

        send_message(current_state)
        last = current_state



# collaborated with thyler and sage on this for some syntax and just help in general.
