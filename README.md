# Simple Keylogger

A basic keylogger in Python that logs keystrokes and sends the captured input via Gmail at a regular interval.

DISCLAIMER: 
This project is a proof of concept for educational purposes only, and is not intended to be used unethically. Use responsibly and respect privacy laws.

## Setup

Clone the repository with the command `git clone repo-url`

Before running the keylogger, you need to log into your Gmail account settings and [generate an app password](https://myaccount.google.com/apppasswords) for the program to use. Once you have the app password, create an `.env` in the directory and enter your Gmail address and app password.

Specify the email you would like logs to be sent to by changing the RECIPIENT variable (you might choose to send logs to yourself).

Specify the interval of time (in seconds) at which you would like email reports to be sent within the `email_timer()` function.

## Usage

Once your credentials and desired parameters are configured properly, run `python3 keylogger.py` and begin typing in the terminal.

An initial email should immediately pop up that alerts incoming keystrokes.

![Initial email alert](https://github.com/kmcg55/simple-keylogger/blob/master/img/startup.jpg)
After the specified interval of time elapses, a second email should arrive with the logged keystrokes in the body of the message.

![Log report example](https://github.com/kmcg55/simple-keylogger/blob/master/img/example.jpg)
#### Possible Improvements
- Fix on release function to properly exit listener
- Handle backspaces gracefully
- Add screengrabbing capabilities
