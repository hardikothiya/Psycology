import math
import random
import smtplib


def send_mail(email):
    digits = "0123456789"
    OTP = ""
    for i in range(6):
        OTP += digits[math.floor(random.random() * 10)]
    otp = OTP + " is your OTP"
    msg = otp

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()

    s.login("hardikothiya01@gmail.com", "deitthyzmsevjwtt")
    s.sendmail('hardikothiya01@gmail.com', email, msg)
    return int(OTP)


