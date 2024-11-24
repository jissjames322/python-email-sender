# Python Email Sender

```python
___________              .__.__      _________                  .___            
\_   _____/ _____ _____  |__|  |    /   _____/ ____   ____    __| _/___________ 
 |    __)_ /     \\__  \ |  |  |    \_____  \_/ __ \ /    \  / __ |/ __ \_  __ \
 |        \  Y Y  \/ __ \|  |  |__  /        \  ___/|   |  \/ /_/ \  ___/|  | \/
/_______  /__|_|  (____  /__|____/ /_______  /\___  >___|  /\____ |\___  >__|   
        \/      \/     \/                  \/     \/     \/      \/    \/   

```
## Overview
This Python script allows you to send emails using SMTP. It supports both plain text and HTML emails, making it versatile for various use cases. The script is designed to be user-friendly and customizable.

## Features
- Send plain text and HTML emails.
- Supports multiple email providers.
- Easy to configure and use.
- Logging of email sending results.

## Prerequisites
- Python (Latest)
- Required libraries: `smtplib`, `email`, `getpass`

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/jissjames322/python-email-sender.git
   cd python-email-sender

## Environment Varaiables

To create an environment variable for storing an app password, follow these general steps based on your operating system:

### For Windows:

1.Open System Properties: Right-click on "**This PC**" or "**My Computer**" and select "**Properties**." Then click on "**Advanced system settings**."

2.Environment Variables: Click on the "**Environment Variables**" button.

3.Add a New Variable:

4.Under "**User variables**" or "**System variables**," click on "**New**."

5.In the "**Variable name**" field, enter a descriptive name for your variable (e.g., APP_PASSWORD).

6.In the "**Variable value**" field, enter your app password.

7.Save Changes: Click "**OK**" to close all dialog boxes.

Accessing the Variable: You can access this variable in your application code using the appropriate method for your programming language. For example, in Python, you can use:

```python
import os
app_password = os.getenv('APP_PASSWORD')
```
## For macOS/Linux:
Open Terminal: Launch the terminal application.

Set the Environment Variable: You can set the variable temporarily by running:

```bash
export APP_PASSWORD="your_app_password"
```
To make it permanent, add the above line to your shell configuration file (e.g., .bashrc, .bash_profile, or .zshrc).

Save Changes: If you modified a configuration file, run:

```bash
source ~/.bashrc  # or the appropriate file
```
Accessing the Variable: Similar to Windows, you can access this variable in your application code. For example, in Python:

```python

import os
app_password = os.getenv('APP_PASSWORD')
```

## Usage

1.Run the script:


```bash
python email_sender.py
```

```python

___________              .__.__      _________                  .___
\_   _____/ _____ _____  |__|  |    /   _____/ ____   ____    __| _/___________
 |    __)_ /     \\__  \ |  |  |    \_____  \_/ __ \ /    \  / __ |/ __ \_  __ \
 |        \  Y Y  \/ __ \|  |  |__  /        \  ___/|   |  \/ /_/ \  ___/|  | \/
/_______  /__|_|  (____  /__|____/ /_______  /\___  >___|  /\____ |\___  >__|
        \/      \/     \/                  \/     \/     \/      \/    \/

Enter your email address: 
Enter your email password (app password if using Gmail): 
Enter the receiver's email address: 
Enter the subject of the email: 
Enter the body of the email: 
Email sent successfully!
```

2.Follow the prompts to enter the sender's email, password, receiver's email, subject, and body of the email.

### Improving

- Adding file attachment soon.



   
