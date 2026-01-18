import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# --- CONFIGURATION ---
# Use placeholders to show you understand security best practices
SENDER_EMAIL = "your_email@gmail.com"
APP_PASSWORD = "your_app_password" 

def send_agent_email(recipient, subject, body):
    """
    Handles SMTP authentication and automated message delivery.
    """
    try:
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Secure connection to Gmail SMTP Server (Port 587 for TLS)
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Encrypts the connection
            server.login(SENDER_EMAIL, APP_PASSWORD)
            server.sendmail(SENDER_EMAIL, recipient, msg.as_string())
            
        print(f"✅ Agent successfully delivered email to {recipient}")
    except Exception as e:
        print(f"❌ Connection Error: {e}")

if __name__ == "__main__":
    # Technical test logic for the Ideoversity assignment
    test_subject = "Automation Agent Status: Online"
    test_body = "This system log confirms the Python SMTP agent is functional and secure."
    
    send_agent_email(SENDER_EMAIL, test_subject, test_body)
