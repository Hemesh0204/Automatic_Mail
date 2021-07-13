import os
import random
import smtplib


def automatic_email():
    Name = input("Enter the recipient's Name >>: ")
    email = input("Enter Reciever's  Email Id >>: ")
    message = (f"Hi {Name}, Hope your doing fine")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("Enter your email address", "Pwd")
    s.sendmail('#######',email, message)
    print("Email has been Sent successfully!")


automatic_email()