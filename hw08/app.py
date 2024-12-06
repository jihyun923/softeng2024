from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('post_list.html')

@app.route("/project")
def blog_list():
    df = pd.read_csv("data.csv")
    post_list = df.to_dict(orient='records')
    return render_template(template_name_or_list='project.html', title = "blog post", posts = post_list)


@app.route('/about_jh')
def about_jh():
    return render_template('kjh.html')

@app.route('/about_sy')
def about_sy():
    return render_template('isy.html')


app.run(debug=True)