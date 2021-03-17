from flask import Flask, render_template
import requests
from datetime import datetime as dt

START_YEAR = '2021'
CURRENT_YEAR = str(dt.now().year)


app = Flask(__name__)


def get_blogs(url):
    response = requests.get(url=url)
    response.raise_for_status()
    return response.json()


@app.route('/')
def home():
    return render_template(
        "index.html",
        blogs=blogs,
        start_year=START_YEAR,
        current_year=CURRENT_YEAR
    )


@app.route('/post/<blog_id>')
def post(blog_id):
    blog_id = int(blog_id) - 1
    return render_template(
        "post.html",
        blog=blogs[blog_id],
        start_year=START_YEAR,
        current_year=CURRENT_YEAR
    )


if __name__ == "__main__":
    blog_url = 'https://api.npoint.io/ed99320662742443cc5b'
    blogs = get_blogs(blog_url)
    # print(blogs)

    app.run(debug=True)

