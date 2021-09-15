import smtplib
import pandas
import datetime as dt
import random
import re


def main():
    name = check_date()
    # if month and day are matched in
    if name:
        prepare_mail_body(name)

def check_date():
    # assign current day and month to variables
    current_month = dt.datetime.today().month
    current_day = dt.datetime.today().day
    # read file containing birthday data
    file = pandas.read_csv('birthdays.csv')
    # check if any value in CSV file contains current month value
    month_check = file[file.month == current_month]
    # if DataFrame is empty (no value found) return False
    if month_check.empty:
        return False
    # if some value is found proceed with checking a day
    else:
        day_check = file[file.day == current_day]
        if day_check.empty:
            return False
        else:
            return day_check.values[0][0]

def prepare_mail_body(name):
    mail_body = ''
    # select random template number
    number = random.randint(1, 3)
    # open template in read mode, because it's contents will be rewritten to string
    with open(f'letter_templates/letter_{number}.txt', mode='r') as letter:
        # define a placeholder
        reg_ex = '\[NAME\]'
        # rewrite each line into the string
        # in case there's a match for placeholder switch it for a name extracted from CSV file
        for line in letter:
            mail_body += re.sub(reg_ex, name, line)
    send_mail(mail_body)

def send_mail(mail_body):
    # sender data
    sender_email = 'testd3369@gmail.com'
    # do not leave blank
    password = ''
    # prepare SMTP connection
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=sender_email, password=password)
        connection.sendmail(
            from_addr=sender_email,
            # do not leave blank
            to_addrs='',
            msg=f"Subject:Happy Birthday!\n\n{mail_body}")

if __name__ == "__main__":
    main()
