import os
import random
import smtplib
from datetime import datetime, time
from email.message import EmailMessage
from api import (
    fetch_facts,
    fetch_jokes,
    fetch_jokes2,
    chuck_norris,
    open_trivia,
    date_facts,
    random_date_facts,
)
from dotenv import load_dotenv

load_dotenv()


# create the email
def email_alert(subject, body, to):
    # message data
    msg = EmailMessage()
    msg["to"] = to
    msg["subject"] = subject
    msg.set_content(body)

    # sender's credentials
    user = os.environ["sender_email"]
    password = os.environ["sender_password"]
    msg["from"] = user

    # server details
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()


# main code
if __name__ == "__main__":
    # choose a subject
    subjects = ["Gentle reminder for medicines💊", "A reminder to take medicines"]
    chosen_subject = random.choice(subjects)

    # chose a salutation depending on time
    now = datetime.now()
    current_time = now.time()
    salutation = (
        "Good afternoon"
        if current_time >= time(8, 00) and current_time <= time(10, 00)
        else "Good evening"
    )

    # chose the email header
    header = [
        "Did you forget about your medicines??.",
        "Happy to remind you about your medicines.",
    ]
    chosen_header = random.choice(header)

    # randomly select one out of many apis
    apis = [
        fetch_facts,
        fetch_jokes,
        fetch_jokes2,
        chuck_norris,
        open_trivia,
        date_facts,
        random_date_facts,
    ]
    chosen_api = random.choice(apis)
    topic, body = chosen_api()

    # send mail
    email_alert(
        chosen_subject,
        salutation
        + " "
        + os.environ["receiver_1_name"]
        + "! ✨\n"
        + chosen_header
        + "\n\n"
        + topic
        + ": "
        + body
        + "\n\nTake care! 😊\n",
        os.environ["receiver_1"],
    )
    email_alert(
        chosen_subject,
        salutation
        + " "
        + os.environ["receiver_2_name"]
        + "! ✨\n"
        + chosen_header
        + "\n\n"
        + topic
        + ": "
        + body
        + "\n\nTake care! 😊\n",
        os.environ["receiver_2"],
    )
