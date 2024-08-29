import schedule
import time
import smtplib
from email.mime.text import MIMEText

def send_email():
    # Email details
    sender = "innoviummall@hotmail.com"
    recipient = "kaprikadeep@gmail.com"
    subject = "Scheduled Email"
    body = "This is a test email sent every minute."

    # Create MIMEText object
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    # Sending the email using SMTP
    try:
        with smtplib.SMTP("smtp-mail.outlook.com", 587) as server:
            server.starttls()  # Secure the connection
            server.login(sender, "WalidEtsy12@")
            server.sendmail(sender, recipient, msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Schedule the job every minute
schedule.every(1).minute.do(send_email)

while True:
    schedule.run_pending()
    time.sleep(1)
