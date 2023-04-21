


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

# function for ping and comparing previous ping status with current.
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

    #create SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    # start TLS for security
    s.starttls()
    # Authentication
    s.login(email, pw)
    # Message 
    message = f"Server is {status.lower()}"
    s.sendmail(email,email, message)
    # Terminate Session
    s.quit()

last = ping_test(target)

#Infinite loops to keep pinging target
while True:
    current_state = ping_test(target)
    if current_state != last:
#calls function 
        send_message(current_state)
        last = current_state

# gives 2 second wait time before continuing loop 
    time.sleep(2)
