from flask import Flask, render_template, request
import requests
import smtplib
import os

app = Flask(__name__)
FROM_MAIL = os.environ.get("TEST_MAIL_100_DAYS")
PASSWORD = os.environ.get("TEST_MAIL_100_DAYS_PASSWORD")
TO_MAIL = FROM_MAIL


@app.route('/')
def main():
    response = requests.get(url="https://api.npoint.io/7b603f609ff43f6820b6")
    blog_data = response.json()
    return render_template('index.html', blog_data=blog_data)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == "POST":
        send_email(data=request.form)
        return render_template('contact.html', data_send=True)
    else:
        return render_template('contact.html', data_send=False)

@app.route('/post/<int:number>')
def post(number):
    response = requests.get(url="https://api.npoint.io/7b603f609ff43f6820b6")
    data = response.json()
    for single_post in data:
        if single_post["id"] == number:
            return render_template('post.html', data=single_post)

def send_email(data):
    name = data['Name']
    email = data["Email"]
    phone = data["Phone"]
    text = data["Message"]

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=FROM_MAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=FROM_MAIL,
            to_addrs=TO_MAIL,
            msg=f"Subject: Blog Contact Form Message!\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {text}")


if __name__ == "__main__":
    app.run(debug=True)
