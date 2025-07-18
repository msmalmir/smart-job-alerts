import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

def send_job_matches_email(
    sender_email, sender_password, receiver_email, job_matches, keyword
):
    message = MIMEMultipart("alternative")
    message["Subject"] = f"Your Daily Matched Job Postings for {keyword} – {timestamp}"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create HTML content
    # Start HTML content
    html = f"<h2>🔍 Matching Results for Keyword: {keyword}</h2>"
    for job in job_matches:
        html += f"""
        <hr>
        <p><b>✅ Match Score:</b> {job.get('score', 'N/A')}</p>
        <p><b>📝 Job Title:</b> {job['title']} at {job['employer']}</p>
        <p><b>🔗 URL:</b> <a href="{job['url']}">{job['url']}</a></p>
        <p><b>💬 Reason:</b> {job['reason']}</p>
        """
    html += "<hr><p style='font-size:small;'>Generated by Smart Job Matcher</p>"
    message.attach(MIMEText(html, "html"))

    # Send email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
