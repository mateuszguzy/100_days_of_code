from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get(url="https://api.npoint.io/9ac20c33562e438c2d92")
    # load all posts, and render their titles and subtitles on home page
    blog_data = response.json()
    return render_template("index.html", blog_data=blog_data)

@app.route('/post/<int:num>')
def get_post(num):
    response = requests.get(url="https://api.npoint.io/9ac20c33562e438c2d92")
    blog_data = response.json()
    # on home page there are redirects to exact post
    # number of post to show is determined by "num" variable and inside JSON in "id" attribute
    # check all posts on the blog and if one's id match "num" variable pass it into HTML templates
    for entry in blog_data:
        if entry["id"] == num:
            post_data = entry
    return render_template("post.html", post_data=post_data)

if __name__ == "__main__":
    app.run(debug=True)
