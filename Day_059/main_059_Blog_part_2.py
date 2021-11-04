from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def main():
    response = requests.get(url="https://api.npoint.io/7b603f609ff43f6820b6")
    blog_data = response.json()
    return render_template('index.html', blog_data=blog_data)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/post/<int:number>')
def post(number):
    response = requests.get(url="https://api.npoint.io/7b603f609ff43f6820b6")
    data = response.json()
    for single_post in data:
        if single_post["id"] == number:
            return render_template('post.html', data=single_post)

if __name__ == "__main__":
    app.run(debug=True)
