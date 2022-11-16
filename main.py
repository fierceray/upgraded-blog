from flask import Flask, render_template, request

import requests

import json

app = Flask(__name__)

result = requests.get("https://api.npoint.io/ef41c5e88b2f49fde56d")
data = json.loads(result.text)
print(data)


@app.route('/')
def get_all_posts():
    return render_template("index.html", posts=data)


@app.route('/contact', methods=['POST', 'get'])
def get_contact():
    if request.method == 'POST':
        print(request.form['user_name'], request.form['user_email'], request.form['user_phone'],
              request.form['user_message'])
        return render_template("contact.html", title='Successfully sent your data')
    if request.method == 'GET':
        return render_template("contact.html", title='Contact Me')


@app.route('/about')
def get_about():
    return render_template("about.html")


@app.route('/post/<int:post_id>')
def get_post(post_id):
    print(post_id)
    print(data[post_id - 1])
    for each_post in data:
        if post_id == each_post['id']:
            request_post = each_post
    return render_template("post.html", post=request_post)


if __name__ == "__main__":
    app.run(debug=True)
