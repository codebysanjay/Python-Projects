import csv
import smtplib


def email_automation():
    with open('test.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            name = row[0]+' '+row[1]
            mail = row[2]
            message = (f"Dear {name},Welcome here")
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login("Your email", "your Password")
            s.sendmail('mail ID', mail, message)
            print('Mailsent')


email_automation()
