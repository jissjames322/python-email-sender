import smtplib #  A built-in Python library for sending emails using the Simple Mail Transfer Protocol (SMTP).
from email.mime.text import MIMEText # MIMEText and MIMEMultipart: Classes from the email.mime module used to create email messages. MIMEMultipart allows for multiple parts (like text and attachments), while MIMEText is specifically for plain text emails.
from email.mime.multipart import MIMEMultipart
import getpass # getpass: A module that provides a secure way to handle password input without echoing it on the screen.

# Function to print text in a specific RGB color using ANSI escape codes
def print_in_color(text, r, g, b): # Takes a string and r,g,b as input
    print(f"\033[38;2;{r};{g};{b}m{text}\033[0m") # Escape which sets the foreground color using RGB values.

def print_banner(): # Some Banner text.
    banner = r"""
___________              .__.__      _________                  .___            
\_   _____/ _____ _____  |__|  |    /   _____/ ____   ____    __| _/___________ 
 |    __)_ /     \\__  \ |  |  |    \_____  \_/ __ \ /    \  / __ |/ __ \_  __ \
 |        \  Y Y  \/ __ \|  |  |__  /        \  ___/|   |  \/ /_/ \  ___/|  | \/
/_______  /__|_|  (____  /__|____/ /_______  /\___  >___|  /\____ |\___  >__|   
        \/      \/     \/                  \/     \/     \/      \/    \/       
"""
    print_in_color(banner, 159, 239, 0)  # RGB values for #9fef00 this is inspired color from hack the box : )

def send_email(sender_email, sender_password, receiver_email, subject, body): # Takes sender email, sender password, receiver email, subject and body as input.
    # Create the email object
    msg = MIMEMultipart() # Create a multipart message (MIMEMULTIPART) to allow for multiple parts (like text).
    msg['From'] = sender_email # Set the sender email.
    msg['To'] = receiver_email # set the receiver email.
    msg['Subject'] = subject # Subject of the email.

    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))

    try: # Handling Exceptions.
        # Connect to the Gmail SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as server: # Connects to smtp server.
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(sender_email, sender_password)  # Log in to the email account
            server.send_message(msg)  # Send the email
            print_in_color("Email sent successfully!", 159, 239, 0)  # RGB values for #9fef00
    except Exception as e:
        print(f"\033[38;2;255;0;0mFailed to send email: {e}\033[0m")  # Red for error messages

if __name__ == "__main__":
    print_banner()  # Display the banner

    # Get email details from the user
    sender_email = input("Enter your email address: ")
    sender_password = getpass.getpass("Enter your email password (app password if using Gmail): ")
    receiver_email = input("Enter the receiver's email address: ")
    subject = input("Enter the subject of the email: ")
    body = input("Enter the body of the email: ")

    # Send the email
    send_email(sender_email, sender_password, receiver_email, subject, body)